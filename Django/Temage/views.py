from django.shortcuts import render
from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.core import serializers

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
    recentpic = Product.objects.filter(pcreator__user__id=identity).values('ptitle', 'pimag')
    collectpic = Collection.objects.filter(user=identity).values('cards__cproduct__ptitle', 'cards__cproduct__pimag', 'cards__curl', 'cards__cprompt')
    gallerypic = Card.objects.all().values('cproduct__ptitle', 'cproduct__pimag', 'curl', 'cprompt')
    
    relist = [list(recentpic), list(collectpic), list(gallerypic)]
    return HttpResponse(json.dumps(relist), content_type="application/json")


def get_work_data(request):
    #if request.user.is_authenticated():
    #identity = request.user.id
    wid=1
    work = Product.objects.get(pid=wid).html
    allstyle = Style.objects.all().values('sid')
    relist = [list(allstyle), work]
    return HttpResponse(json.dumps(relist), content_type="application/json")
    


def get_gallery_data(request):
    #if request.user.is_authenticated():
    #identity = request.user.id
    identity = 1
    cards =  Card.objects.values('cproduct__ptitle', 'cproduct__pimag', 'curl', 'cprompt')
    return HttpResponse(json.dumps(list(cards)), content_type="application/json")


def get_collection_data(request):
    #if request.user.is_authenticated():
    #identity = request.user.id
    identity = 1
    collections = Collection.objects.filter(user__id=identity).values('cards__cproduct__ptitle', 'cards__cproduct__pimag', 'cards__curl', 'cards__cprompt')
    return HttpResponse(json.dumps(list(collections)), content_type="application/json")

def get_rescent_data(request):
    #if request.user.is_authenticated():
    #identity = request.user.id
    identity =  1
    recentpic = Product.objects.filter(pcreator=identity).values('ptitle', 'pimag')
    return HttpResponse(json.dumps(list(recentpic)), content_type="application/json")
    