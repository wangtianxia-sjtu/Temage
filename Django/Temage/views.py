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



# Create your views here.
def get_user(request, num):
    
    user = User.objects.get(id=int(num))
    json_data = serializers.serialize('json', [user,])
    json_data = json.loads(json_data)
    result = json.dumps(json_data[0]).replace('\"',"\'")
    return HttpResponse(json.dumps(result), content_type="application/json")

def get_homepage_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    user = Profile.objects.get(user__id=identity)
    recentpic = user.cards.all()[:2].values('product__title', 'product__imagesrc', 'url', 'prompt')
    collectpic = user.collections.all()[:2].values('cards__product__title', 'cards__product__imagesrc', 'cards__url', 'cards__prompt')
    intrests = list(user.theme.all().values('id')) 
    gallerypic = Card.objects.filter(product__theme__id=intrests[0]['id'])[:2].values('product__title', 'product__imagesrc', 'url', 'prompt')
    relist = [list(recentpic), list(collectpic), list(gallerypic)]
    return HttpResponse(json.dumps(relist), content_type="application/json")

def get_work_data(request, workID):
    # guess data
    work = Product.objects.get(id=workID).html
    allstyle = Style.objects.all().values('name')
    relist = [list(allstyle), work]
    return HttpResponse(json.dumps(relist), content_type="application/json")
    


def get_gallery_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    cards =  Card.objects.values('product__title', 'product__imagesrc', 'url', 'prompt')
    return HttpResponse(json.dumps(list(cards)), content_type="application/json")


def get_collection_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    collectionlist = Profile.objects.get(user__id=identity).collections.all()
    collections = []
    for col in collectionlist:
        cards  = col.cards.all()
        cardsInfo = {}
        for card in cards:
            userInfo = {}
            userInfo['username'] = card.creator.user.username
            userInfo['id'] = card.creator.user.id
            userInfo['avator'] = card.creator.avator
            userInfo = list(card.creator.values('user__username', 'user__id', 'avator')
            cardInfo['name'] = card.product.title
            cardInfo['imagesrc'] = card.product.imagesrc
            cardInfo['prompt'] = card.prompt
            cardInfo['url'] = card.url
            cardInfo['creator'] = userInfo
            cardInfo['title'] = card.title
            cardsInfo.append(cardInfo)
        collections.append(cardsInfo)
    return HttpResponse(json.dumps(list(collections)), content_type="application/json")

def get_rescent_data(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    recentpic = Product.objects.filter(creator=identity).values('title', 'imagesrc')
    return HttpResponse(json.dumps(list(recentpic)), content_type="application/json")
    
def login_submit(request):
    if (request.method == 'POST'):
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
            return HttpResponse(
              jwt.encode(payload, "Temage"),
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

# for models test by hand
def test(request):
    user = Profile.objects.get(user__id=1)
    themelist = user.theme.all().values('name')
    productlist = user.products.all().values('title')
    collectionlist = user.collections.all()
    collections = []
    print(type(collectionlist))
    for col in collectionlist:
        cards  = col.cards.all()
        cardinfo = []
        for card in cards:
            cardinfo.append([card.title, card.prompt])
        collections.append([col.name, cardinfo])
    relist = [list(themelist), list(productlist), collections]
    return HttpResponse(json.dumps(relist), content_type="application/json")
