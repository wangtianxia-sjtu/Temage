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
    userInfo = {}
    userInfo['username'] = user.user.username
    userInfo['id'] = user.user.id
    userInfo['avator'] = str(user.avator)
    relist = {}
    relist['recent_pics'] = reclist
    relist['collect_pics'] = collist[1]
    relist['gallery_pics'] = gallist
    relist['user_info'] = userInfo
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
    work_data = {}
    work_data['guess_style'] = [{'name' : 'sport','possibility': '80%'},{'name' : 'art','possibility' : '45%'},{'name' : 'history','possibility': '25%'}]
    work_data['style'] = ['style_1','style_2','style_4','style_5','style_6','style_7','style_8','style_9','style_a','style_b','style_c','style_d','style_e','style_f','style_g','style_h','style_i','style_j','style_k','style_l']
    work_data['temage'] = "<html><head> </head> <body> <h1>Hello, Temage!</h1> </body> </html>"
    return HttpResponse(json.dumps(work_data), content_type="application/json")

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
    if cards.count() > 7:
        cards = cards[:7]

    for card in cards:
        cardinfo = {}
        userInfo = {}
        userInfo['username'] = card.creator.user.username
        userInfo['id'] = card.creator.user.id
        userInfo['avator'] = str(card.creator.avator)
        cardinfo['id'] = card.product.id
        cardinfo['creator'] = userInfo
        cardinfo['title'] = card.title
        cardinfo['imagesrc'] = str(card.product.imagesrc)
        cardinfo['head'] = card.head
        cardinfo['maintext'] = card.prompt
        cardinfo['foottext'] = card.foottext
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
        cardinfo['id'] = card.product.id
        cardinfo['creator'] = userInfo
        cardinfo['imagesrc'] = str(card.product.imagesrc)
        cardinfo['title'] = card.title
        cardinfo['head'] = card.head
        cardinfo['maintext'] = card.prompt
        cardinfo['foottext'] = card.foottext
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
    return HttpResponse(json.dumps(collections[1]), content_type="application/json")

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
        card_id = json.loads(request.body)['id']
        card = Card.objects.get(id=card_id)
        content = {}
        userInfo = {}
        userInfo['username'] = card.creator.user.username
        userInfo['id'] = card.creator.user.id
        userInfo['avator'] = str(card.creator.avator)
        content['id'] = card_id
        content['text'] = card.product.html
        content['creator'] = userInfo
        content['title'] = card.title
        themes = card.product.theme.all()
        themelist = []
        for theme in themes:
            themelist.append(theme.name)
        content['style'] = themelist
        return HttpResponse(json.dumps(content), content_type="application/json")

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
            interests = post_body['interest']
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user)
            for interest in interests:
                theme = Theme.objects.get(name=interest)
                profile.theme.add(theme)

            avator = open("../media/img/avator/boy.jpg", "rb")
            profile.avator.save('boy.jpg', File(avator), save=True)
            return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
        else:
            return HttpResponse(json.dumps("The username has been used"),
                                status=400,
                                content_type="application/json"
                                )

##########################
# Interface for workflow
##########################
def pic_post(request):
    """
    Get pictures from users, and send them to the models.
    """
    
    return HttpResponse()

def text_post(request):
    """
    Get text content from users, and send it with the pictures
    """

    return HttpResponse()

def ret_html(request, style):

    return HttpResponse()

def store_passage(request):

    return HttpResponse()

def finished_work(request):

    return HttpResponse()

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
