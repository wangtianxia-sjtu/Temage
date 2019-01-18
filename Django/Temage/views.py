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
    #if request.user.is_authenticated():
    #identity = request.user.id
    identity = 1
    recentpic = Product.objects.filter(creator__user__id=identity).values('title', 'imag')
    collectpic = Collection.objects.filter(user__user__id=identity).values('cards__product__title', 'cards__product__imag', 'cards__url', 'cards__prompt')
    gallerypic = Card.objects.all().values('product__title', 'product__imag', 'url', 'prompt')
    
    relist = [list(recentpic), list(collectpic), list(gallerypic)]
    return HttpResponse(json.dumps(relist), content_type="application/json")


def get_work_data(request):
    #if request.user.is_authenticated():
    #identity = request.user.id
    wid=1
    work = Product.objects.get(id=wid).html
    allstyle = Style.objects.all().values('id')
    relist = [list(allstyle), work]
    return HttpResponse(json.dumps(relist), content_type="application/json")
    


def get_gallery_data(request):
    #if request.user.is_authenticated():
    #identity = request.user.id
    identity = 1
    cards =  Card.objects.values('product__title', 'product__imag', 'url', 'prompt')
    return HttpResponse(json.dumps(list(cards)), content_type="application/json")


def get_collection_data(request):
    identity = 1
    collections = Collection.objects.filter(user__user__id=identity).values('cards__product__title', 'cards__product__imag', 'cards__url', 'cards__prompt')
    return HttpResponse(json.dumps(list(collections)), content_type="application/json")

def get_rescent_data(request):
    identity =  1
    recentpic = Product.objects.filter(creator=identity).values('title', 'imag')
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
def setupdb(request):
    img1 = open("../test_file/img/good.jpg", "rb")
    img2 = open("../test_file/img/bad.jpg", "rb")
    User.objects.create_user(id=1,username=1234, is_superuser=True, email='1234@qq.com', password="1234")
    user1 = User.objects.create_user(username="qxy", password="123", id=1)
    user2 = User.objects.create_user(username="wxm", password="123")
    style1 = Style.objects.create(name="style_1")
    style2 = Style.objects.create(name="style_2", id=2)
    theme1 = Theme.objects.create(name="theme_1", id=1)
    theme2 = Theme.objects.create(name="theme_2", id=2)
    profile1 = Profile.objects.create(user = user1, phone = "+8618217508975", sex = 1)
    profile2 = Profile.objects.create(user = user2, phone = "+8612334443223", sex = 0)
    profile1.interest.add(theme1)
    profile1.interest.add(theme2)
    product1 = Product.objects.create(title="product_1", html="<p>good day</p>", creator=profile1,style=style1, score=0.1)
    product2 = Product.objects.create(title="product_2", html="<p>bad day</p>", creator=profile1,style=style2, score=0.9)
    product1.imag.save('good.jpg', File(img1), save=True)
    product2.imag.save('bad.jpg', File(img2), save=True)
    product1.theme.add(theme1)
    product2.theme.add(theme2)
    card1 = Card.objects.create(product=product1, url="http://temage/goodday", title="positive", prompt="A positive people said...")
    card2 = Card.objects.create(product=product2, url="http://temage/goodday", title="negative", prompt="A negative people said...")
    collection = Collection.objects.create(name = "quote", user=profile1)
    collection.cards.add(card1)
    collection.cards.add(card2)
    return HttpResponse(json.dumps("succeed"), content_type="application/json")

def cleardb(request):
    Style.objects.all().delete()
    Theme.objects.all().delete()
    Profile.objects.all().delete()
    User.objects.all().delete()
    Product.objects.all().delete()
    Card.objects.all().delete()
    Collection.objects.all().delete()
    return HttpResponse(json.dumps("succeed"), content_type="application/json")
