from django.shortcuts import render
from Temage.models import *
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.contrib.auth import authenticate, login
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.files import File
import jwt
import random
import requests

####################################################################
# Interfaces for register and login, and also identity authenticate
####################################################################
def homepage_data(request):
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
        card_info['imgsrc'] = str(card.product.image_src)
        card_info['promt'] = card.prompt
        card_info['id'] = card.product.id
        reclist.append(card_info)
    collection = user.collection
    cards = collection.cards.all()
    cards_info = []
    for card in cards:
        card_info = {}
        card_info['title'] = card.product.title
        card_info['imgsrc'] = str(card.product.image_src)
        card_info['prompt'] = card.prompt
        card_info['id'] = card.product.id
        cards_info.append(card_info)
    intrests = list(user.theme.all().values('id'))
    cards = Card.objects.filter(product__theme__id=intrests[0]['id'])[:2]
    gallist = []
    for card in cards:
        card_info = {}
        card_info['title'] = card.product.title
        card_info['imgsrc'] = str(card.product.image_src)
        card_info['promt'] = card.prompt
        card_info['id'] = card.product.id
        gallist.append(card_info)
    user_info = {}
    user_info['username'] = user.user.username
    user_info['id'] = user.user.id
    user_info['avator'] = str(user.avator)
    relist = {}
    relist['recent_pics'] = reclist
    relist['collect_pics'] = cards_info
    relist['gallery_pics'] = gallist
    relist['user_info'] = user_info
    return HttpResponse(json.dumps(relist), content_type="application/json")

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

            avator = open("../test_file/img/boy.jpg", "rb")
            profile.avator.save('boy.jpg', File(avator), save=True)
            return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
        else:
            return HttpResponse(json.dumps("The username has been used"),
                                status=400,
                                content_type="application/json"
                                )

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



####################################################################
# Interfaces for get data from database and send theme to front-end
####################################################################

def gallery_data(request):
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
    cards_info = []
    if cards.count() > 7:
        cards = cards[:7]

    for card in cards:
        card_info = {}
        user_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['title'] = card.title
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['head'] = card.head
        card_info['maintext'] = card.prompt
        card_info['foottext'] = card.foot_text
        cards_info.append(card_info)
    return HttpResponse(json.dumps(cards_info), content_type="application/json")

def gallery_more_cards(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    cards = Card.objects.order_by('?')[:4]
    cards_info = []
    for card in cards:
        card_info = {}
        user_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['title'] = card.title
        card_info['head'] = card.head
        card_info['maintext'] = card.prompt
        card_info['foottext'] = card.foot_text
        cards_info.append(card_info)
    return HttpResponse(json.dumps(cards_info), content_type="application/json")

def post_search(request):
    keywords = json.loads(request.body)['keywords']
    data = {"size": 10, "query": { "bool":{  "should":[{"terms":{"style":keywords.split()}},{"match":{"title": keywords}}]} }}
    response = requests.post(settings.ES_SEARCH_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    ids = []
    res_data = json.loads(response.text)
    for hit in res_data['hits']['hits']:
        ids.append(hit['_source']['ID'])
    cards = Card.objects.filter(id__in = ids)
    cards_info = []
    for card in cards:
        card_info = {}
        user_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['title'] = card.title
        card_info['head'] = card.head
        card_info['maintext'] = card.prompt
        card_info['foottext'] = card.foot_text
        cards_info.append(card_info)
    return HttpResponse(json.dumps({"cards":cards_info}), content_type="application/json")
    

def collection_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    collection = Profile.objects.get(user__id=identity).collection
    cards = collection.cards.all()
    cards_info = []
    for card in cards:
        user_info = {}
        card_info = {}
        user_info['username'] = card.creator.user.username
        user_info['id'] = card.creator.user.id
        user_info['avator'] = str(card.creator.avator)
        card_info['name'] = card.product.title
        card_info['imagesrc'] = str(card.product.image_src)
        card_info['prompt'] = card.prompt
        card_info['id'] = card.product.id
        card_info['creator'] = user_info
        card_info['title'] = card.title
        cards_info.append(card_info)
    return HttpResponse(json.dumps(cards_info), content_type="application/json")

def recent_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    recentpic = Profile.objects.get(user__id=identity).cards.all()[:4]
    reclist = []
    for pic in recentpic:
        picinfo = {}
        picinfo['title'] = pic.product.title
        picinfo['img_url'] = str(pic.product.image_src)
        picinfo['promt'] = pic.prompt
        picinfo['id'] = pic.product.id
        reclist.append(picinfo)
    return HttpResponse(json.dumps(reclist), content_type="application/json")

def text(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']
        product_id = json.loads(request.body)['id']
        product = Product.objects.get(id=product_id)
        content = {}
        userInfo = {}
        userInfo['username'] = product.creator.user.username
        userInfo['id'] = product.creator.user.id
        userInfo['avator'] = str(product.creator.avator)
        if product.creator.user.id == identity:
            content['can_be_delete'] = 1
        else:
            content['can_be_delete'] = 0
        user = Profile.objects.get(user__id=identity)
        collect = user.collections.get(id=1)
        been_owned = collect.cards.filter(product_id = product_id)
        if been_owned:
            content['has_been_colleted'] = 1
        else:
            content['has_been_collected'] = 0
        content['id'] = product_id
        content['text'] = product.html
        content['creator'] = product.creator
        content['title'] = product.title
        themes = product.theme.all()
        themelist = []
        for theme in themes:
            themelist.append(theme.name)
        content['style'] = themelist
        return HttpResponse(json.dumps(content), content_type="application/json")

def collect(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']
        post_body = json.loads(request.body)
        card_id = post_body['id']
        try:
            user = Profile.objects.get(user__id=identity)
            card = Card.objects.get(product__id=card_id)
            collection = user.collection
            collection.cards.add(card)
            return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
        except:
            return HttpResponse(json.dumps("failed"), status=400, content_type="application/json")

def delete_product(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)
        work_id = post_body['workID']
        try:
            product = Product.objects.get(id = work_id)
            product.delete()
            # ES delete start
            # response = requests.post(settings.ES_DELETE_URL, data=json.loads({"query":{"match":{"ID": work_id}}}), headers={"content-type":"application/json"})
            # if response.status_code != 200:
            #     raise RuntimeError('Index has not been deleted!')
            # ES delete end
            return HttpResponse(json.dumps("succeed"), status = 200, content_type = "application/json")
        except:
            return HttpResponse(json.dumps("error"), status = 400, content_type = "application/json")

def cancel_collect(request):
    if request.method == 'POST':
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']

        user = Profile.objects.get(user__id=identity)

        post_body = json.loads(request.body)
        work_id = post_body['id']
        try:
            card = Card.objects.get(product__id=work_id)
            collection = user.collection
            if (collection.cards.filter(product__id=work_id).count() == 0):
                return HttpResponse(json.dumps("This work has already been removed!"), status = 402, content_type = "application/json")
            else:
                card.collections.remove(collection)
                return HttpResponse(json.dumps("Succeed"), status=200, content_type = "application/json")
        except:
            return HttpResponse(json.dumps("Something wrong"), status = 400, content_type="application/json")
