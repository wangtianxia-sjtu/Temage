from django.shortcuts import render
from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Theme
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
import jwt
import random


# Create your views here.

####################################################################
# Interfaces for get data from database and send theme to front-end
####################################################################

def get_homepage_data(request):
    """
    This is function that gets data for the homepage.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required homepage data in json-string form.
    """
    identity = jwt.decode(request.META.get("HTTP_AUTHORIZATION"), "Temage")['id']
    user = Profile.objects.get(user__id=identity)
    recentpic = user.cards.all()[:2]
    reclist = []
    for card in recentpic:
        card_info = {}
        card_info['title'] = card.product.title
        card_info['imgsrc'] = str(card.product.imagesrc)
        card_info['promt'] = card.prompt
        card_info['id'] = card.product.id
        reclist.append(card_info)
    collectionlist = user.collections.all()[:2]
    collist = []
    for col in collectionlist:
        cards = col.cards.all()
        cards_info = []
        for card in cards:
            card_info = {}
            card_info['title'] = card.product.title
            card_info['imgsrc'] = str(card.product.imagesrc)
            card_info['prompt'] = card.prompt
            card_info['id'] = card.product.id
            cards_info.append(card_info)
        collist.append(cards_info)
    intrests = list(user.theme.all().values('id'))
    cards = Card.objects.filter(product__theme__id=intrests[0]['id'])[:2]
    gallist = []
    for card in cards:
        card_info = {}
        card_info['title'] = card.product.title
        card_info['imgsrc'] = str(card.product.imagesrc)
        card_info['promt'] = card.prompt
        card_info['id'] = card.product.id
        gallist.append(card_info)
    relist = [reclist, collist, list(gallist)]
    return HttpResponse(json.dumps(relist), content_type="application/json")

def get_work_data(request, work_id):
    """
    This is function that gets data for the work space.
    Parameters:
        work_id - this is a request to data from the front-end.
    Returns:
        required homepage data in json-string form.
    """
    # guess data here
    work = Product.objects.get(id=work_id).html
    allstyle = Style.objects.all().values('name')
    relist = [list(allstyle), work]
    return HttpResponse(json.dumps(relist), content_type="application/json")

def get_gallery_data(request):
    """
    This is function that gets data for the work space.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required homepage data in json-string form.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    cards = Card.objects.all()
    cardsInfo = []
    if cards.count() >= 7:
        cards = cards[:7]

    for card in cards:
        cardinfo = {}
        userInfo = {}
        userInfo['username'] = card.creator.user.username
        userInfo['id'] = card.creator.user.id
        userInfo['avator'] = str(card.creator.avator)
        cardinfo['prompt'] = card.prompt
        cardinfo['id'] = card.product.id
        cardinfo['creator'] = userInfo
        cardinfo['title'] = card.title
        cardsInfo.append(cardinfo)
    return HttpResponse(json.dumps(cardsInfo), content_type="application/json")

def get_gallery_more_cards(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    cards = Card.objects.order_by('?')[:4]
    cardsInfo = []
    for card in cards:
        cardinfo = {}
        userInfo = {}
        userInfo['username'] = card.creator.user.username
        userInfo['id'] = card.creator.user.id
        userInfo['avator'] = str(card.creator.avator)
        cardinfo['prompt'] = card.prompt
        cardinfo['id'] = card.product.id
        cardinfo['creator'] = userInfo
        cardinfo['title'] = card.title
        cardsInfo.append(cardinfo)
    return HttpResponse(json.dumps(cardsInfo), content_type="application/json")

def get_collection_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    collectionlist = Profile.objects.get(user__id=identity).collections.all()
    collections = []
    for col in collectionlist:
        cards = col.cards.all()
        cardsInfo = []
        for card in cards:
            userInfo = {}
            cardinfo = {}
            userInfo['username'] = card.creator.user.username
            userInfo['id'] = card.creator.user.id
            userInfo['avator'] = str(card.creator.avator)
            cardinfo['name'] = card.product.title
            cardinfo['imagesrc'] = str(card.product.imagesrc)
            cardinfo['prompt'] = card.prompt
            cardinfo['id'] = card.product.id
            cardinfo['creator'] = userInfo
            cardinfo['title'] = card.title
            cardsInfo.append(cardinfo)
        collections.append(cardsInfo)
    return HttpResponse(json.dumps(collections), content_type="application/json")

def get_rescent_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    recentpic = Profile.objects.get(user__id=identity).cards.all()[:4]
    reclist = []
    for pic in recentpic:
        picinfo = {}
        picinfo['title'] = pic.product.title
        picinfo['img_url'] = str(pic.product.imagesrc)
        picinfo['promt'] = pic.prompt
        picinfo['id'] = pic.product.id
        reclist.append(picinfo)
    return HttpResponse(json.dumps(reclist), content_type="application/json")

def get_text(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        card_id = post_body['id']
        card = Card.objects.get(id=card_id)
        cardinfo = {}
        userinfo = {}
        userinfo['username'] = card.creator.user.username
        userinfo['id'] = card.creator.user.id
        userinfo['avator'] = str(card.creator.avator)
        cardinfo['id'] = card.id
        cardinfo['text'] = card.product.html
        cardinfo['creator'] = userinfo
        cardinfo['title'] = card.product.title
        cardinfo['style'] = card.product.style.name
        return HttpResponse(json.dumps(cardinfo), content_type="application/json")

####################################################################
# Interfaces for register and login, and also identity authenticate
####################################################################

def login_submit(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        username = post_body['username']
        password = post_body['password']
        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            return HttpResponse(status=400)
        if user:
            payload = {
                'id': user.id,
                'name': user.username,
            }
            return HttpResponse(jwt.encode(payload, "Temage"),
                                status=200,
                                content_type="application/json"
                                )

def JWTauthenticate(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        payload = jwt.decode(post_body['token'], "Temage")
        try:
            user = User.objects.get(id=payload['id'])
        except:
            return HttpResponse(status=400)
        else:
            return HttpResponse(
                json.dumps({"username":user.username}),
                status=200,
                content_type="application/json"
                )

def register(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        user = Profile.objects.filter(user__username=post_body['username'])
        if user.count() == 0:
            password = post_body['password']
            username = post_body['username']
            sex = int(post_body['sex'])
            avator = str(post_body['avator'])
            phone = post_body['phone']
            user = User.objects.create_user(username=username, password=password)
            img = open(avator, "rb")
            profile = Profile.objects.create(user=user, sex=sex, phone=phone)
            profile.avator.save('boy.jpg', File(img), save=True)
            return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
        else:
            return HttpResponse(json.dumps("The username has been used"),
                                status=400,
                                content_type="application/json"
                                )

##########################
# Interface for workflow
##########################

# for models test by hand
def test(request):
    user = Profile.objects.get(user__id=1)
    themelist = user.theme.all().values('name')
    productlist = user.products.all().values('title')
    collectionlist = user.collections.all()
    collections = []
    print(type(collectionlist))
    for col in collectionlist:
        cards = col.cards.all()
        cardinfo = []
        for card in cards:
            cardinfo.append([card.title, card.prompt])
        collections.append([col.name, cardinfo])
    relist = [list(themelist), list(productlist), collections]
    return HttpResponse(json.dumps(relist), content_type="application/json")
