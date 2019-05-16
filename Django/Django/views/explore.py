#-*-coding:utf-8-*-
from django.shortcuts import render

from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Theme
from Temage.models import Cache

from django.forms.models import model_to_dict

from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.http import require_GET, require_POST

from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.core import serializers
from django.core.files.base import ContentFile
from django.core.files import File

from django.conf import settings

import json
import jwt
import random
import requests

####################################################################
# Interfaces for register and login, and also identity authenticate
####################################################################
@require_GET
def get_homepage_data(request):
    """
    Gets data for the homepage.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required homepage data in json-string form.
    """
    try:
        identity = jwt.decode(request.META.get("HTTP_AUTHORIZATION"), "Temage")['id']
        user = Profile.objects.get(user__id=identity)
        recentpic = user.cards.all()[:2]
        reclist = []
        for card in recentpic:
            card_info = {}
            card_info['title'] = card.product.title
            card_info['imgsrc'] = "http://202.120.40.109:19132/media/" + str(card.product.image_src)
            card_info['promt'] = card.prompt
            card_info['id'] = card.product.id
            reclist.append(card_info)
        collection = user.collection
        cards = collection.cards.all()
        cards_info = []
        for card in cards:
            card_info = {}
            card_info['title'] = card.product.title
            card_info['imgsrc'] = "http://202.120.40.109:19132/media/" + str(card.product.image_src)
            card_info['prompt'] = card.prompt
            card_info['id'] = card.product.id
            cards_info.append(card_info)
        intrests = list(user.theme.all().values('id'))
        cards = Card.objects.filter(product__theme__id=intrests[0]['id'])[:2]
        gallist = []
        for card in cards:
            card_info = {}
            card_info['title'] = card.product.title
            card_info['imgsrc'] = "http://202.120.40.109:19132/media/" + str(card.product.image_src)
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
        return HttpResponse(json.dumps(relist), status=200, content_type="application/json")
    except:
        return HttpResponse(json.dumps("something wrong!"), status=400, content_type="application/json")

@require_POST
def post_register(request):
    """
    Sign up an account.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of the result.
    """
    post_body = json.loads(request.body.decode('utf-8'))
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

        avator = open("./test_file/img/boy.jpg", "rb")
        profile.avator.save('boy.jpg', File(avator), save=True)

        collection = Collection.objects.create(user=profile, name="收藏夹")
        cache = Cache.objects.create(user=profile)

        return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
    else:
        return HttpResponse(json.dumps("The username has been used"),
                            status=400,
                            content_type="application/json"
                            )
@require_POST
def post_login_submit(request):
    """
    Sign up an account.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of the result.
    """
    post_body = json.loads(request.body.decode('utf-8'))
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
@require_POST
def post_jwt_authenticate(request):
    """
    Tests and verifies the current user's identification.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of the result.
    """
    post_body = json.loads(request.body.decode('utf-8'))
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
@require_GET
def get_gallery_data(request):
    """
    Gets data for the gallery.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required gallery data in json-string form.
    """
    try:
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
            card_info['imagesrc'] = "http://202.120.40.109:19132/media/" + str(card.product.image_src)
            card_info['head'] = card.head
            card_info['maintext'] = card.prompt
            card_info['foottext'] = card.foot_text
            cards_info.append(card_info)
        return HttpResponse(json.dumps(cards_info), status=200, content_type="application/json")
    except:
        return HttpResponse(json.dumps("something wrong"), status=400, content_type="application/json")

@require_GET
def get_gallery_more_cards(request):
    """
    Gets data for the gallery's next page.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required another gallery data in json-string form.
    """
    try:
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
            card_info['imagesrc'] = "http://202.120.40.109:19132/media/" + str(card.product.image_src)
            card_info['title'] = card.title
            card_info['head'] = card.head
            card_info['maintext'] = card.prompt
            card_info['foottext'] = card.foot_text
            cards_info.append(card_info)
        return HttpResponse(json.dumps(cards_info), status=200, content_type="application/json")
    except:
        return HttpResponse(json.dumps("something wrong"), status=400, content_type="application/json")

@require_POST
def post_search(request):
    """
    Gets data for global search.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required data in json-string form.
    """
    try:
        keywords = json.loads(request.body.decode('utf-8'))['keywords']
        data = {
        	"size": 10,
        	"query": {
        		"bool": {
        			"should": [{
        				"terms": {
        					"style": keywords.split()
        				}
        			}, 
        			{
        				"match": {
                "title": {
                  "query":     keywords,
                  "fuzziness": "AUTO",
                  "operator":  "and"
                }
            }
        			}
        			]
        		}
        	}
        }
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
            card_info['imagesrc'] = "http://202.120.40.109:19132/media/" + str(card.product.image_src)
            card_info['title'] = card.title
            card_info['head'] = card.head
            card_info['maintext'] = card.prompt
            card_info['foottext'] = card.foot_text
            cards_info.append(card_info)
        return HttpResponse(json.dumps({"cards":cards_info}), status=200, content_type="application/json")
    except:
        return HttpResponse(json.dumps("something wrong"), status=400, content_type="application/json")
    
@require_GET
def get_collection_data(request):
    """
    Gets informations of user's collection.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required gallery data in json-string form.
    """
    try:
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
            card_info['imagesrc'] = "http://202.120.40.109:19132/media/" + str(card.product.image_src)
            card_info['prompt'] = card.prompt
            card_info['id'] = card.product.id
            card_info['creator'] = user_info
            card_info['title'] = card.title
            cards_info.append(card_info)
        return HttpResponse(json.dumps(cards_info), status=200, content_type="application/json")
    except:
        return HttpResponse(json.dumps("something wrong"), status=400, content_type="application/json")

@require_GET
def get_recent_data(request):
    """
    Gets informations of user's recent modified works.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required recent work data in json-string form.
    """
    try:
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']
        recentpic = Profile.objects.get(user__id=identity).cards.all()[:4]
        reclist = []
        for pic in recentpic:
            picinfo = {}
            picinfo['title'] = pic.product.title
            picinfo['img_url'] = "http://202.120.40.109:19132/media/" + str(pic.product.image_src)
            picinfo['promt'] = pic.prompt
            picinfo['id'] = pic.product.id
            reclist.append(picinfo)
        return HttpResponse(json.dumps(reclist), status=200, content_type="application/json")
    except:
        return HttpResponse(json.dumps("something wrong"), status=400, content_type="application/json")

@require_POST
def get_product(request):
    """
    Gets detailed information of product.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        required detailed work data in json-string form.
    """
    try:
        token = request.META.get("HTTP_AUTHORIZATION")
        payload = jwt.decode(token, "Temage")
        identity = payload['id']
        product_id = json.loads(request.body.decode('utf-8'))['productID']
        product = Product.objects.get(id=product_id)
        content = {}
        user_info = {}
        user_info['username'] = product.creator.user.username
        user_info['id'] = product.creator.user.id
        user_info['avator'] = "http://202.120.40.109:19132/media/" + str(product.creator.avator)
        if product.creator.user.id == identity:
            content['can_be_delete'] = 1
        else:
            content['can_be_delete'] = 0
        user = Profile.objects.get(user__id=identity)
        collect = user.collection
        been_owned = collect.cards.filter(product_id = product_id)
        if been_owned:
            content['has_been_colleted'] = 1
        else:
            content['has_been_collected'] = 0
        content['id'] = product_id
        content['text'] = product.html
        content['creator'] = user_info
        content['title'] = product.title
        themes = product.theme.all()
        themelist = []
        for theme in themes:
            themelist.append(theme.name)
        content['style'] = themelist
        return HttpResponse(json.dumps(content), status=200, content_type="application/json")
    except:
        return HttpResponse(json.dumps("something wrong"), status=400, content_type="application/json")

@require_POST
def post_collect(request):
    """
    Collects the work that the user interested in into his collection.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of this action.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    post_body = json.loads(request.body.decode('utf-8'))
    product_id = post_body['productID']
    # try:
    user = Profile.objects.get(user__id=identity)
    card = Card.objects.get(product__id=product_id)
    collection = user.collection
    collection.cards.add(card)
    # start refresh history
    cards = collection.cards.all()[:3]
    vectors = []
    for card in cards:
        vector = card.product.vector
        if (vector != ''):
            vectors.append(card.product.vector)
    vector_len = len(vectors)
    while vector_len != 3:
        vector_len += 1
        vectors.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    results = []
    results.append(vectors)
    response = requests.post(settings.SERVERB_HISTORIES_URL, data=json.dumps({"histories": results}), headers={"content-type":"application/json"})
    user.vector = response.text
    user.save()
    # end refresh history
    return HttpResponse(json.dumps("succeed"), status=200, content_type="application/json")
    # except:
    #     return HttpResponse(json.dumps("failed"), status=400, content_type="application/json")


def delete_product(request):
    """
    Deletes the product completely from the database.
    Parameters:
        request - this is a request to data from the front-end. 
    Returns:
        status code of this action.
    """
    post_body = json.loads(request.body.decode('utf-8'))
    product_id = post_body['productID']
    try:
        product = Product.objects.get(id = product_id)
        product.delete()
        # ES delete start
        data = {
            "query": {
                "match": {
                    "ID": product_id
                }
            }
        }
        response = requests.post(settings.ES_DELETE_URL, data=json.dumps(data), headers={"content-type":"application/json"})
        if response.status_code != 200:
            raise RuntimeError('Index has not been deleted!')
        # ES delete end
        return HttpResponse(json.dumps("succeed"), status = 200, content_type = "application/json")
    except:
        return HttpResponse(json.dumps("error"), status = 400, content_type = "application/json")

@require_POST
def cancel_collect(request):
    """
    Removed the card from user's collection
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of this action.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']

    user = Profile.objects.get(user__id=identity)

    post_body = json.loads(request.body.decode('utf-8'))
    product_id = post_body['productID']
    try:
        card = Card.objects.get(product__id=product_id)
        collection = user.collection
        if (collection.cards.filter(product__id=product_id).count() == 0):
            return HttpResponse(json.dumps("This product has already been removed!"), status = 402, content_type = "application/json")
        else:
            card.collections.remove(collection)
            return HttpResponse(json.dumps("Succeed"), status=200, content_type = "application/json")
    except:
        return HttpResponse(json.dumps("Something wrong"), status = 400, content_type="application/json")
