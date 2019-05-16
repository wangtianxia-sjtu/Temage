#-*-coding:utf-8-*-
from django.shortcuts import render

from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Theme

from django.forms.models import model_to_dict

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse

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
import os
import pdfkit
import datetime



##########################
# Interface for workflow
##########################
@require_POST
def post_picture(request): # 需完善
    """
    Posts pictures to the model that inserts pictures into the text.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
       status code of this action.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    # identity = 2
    cache = Profile.objects.get(user__id=identity).cache
    imgs = request.FILES.getlist("file")
    prev_urls = json.loads(cache.imgs_urls)
    if len(imgs) != 0:
        for img in imgs:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            img_name = str(nowTime) + img.name
            file_url = os.path.abspath(settings.MEDIA_ROOT + '/img/imgs/' + img_name)
            destination = open(file_url,'wb')
            for chunk in img.chunks(): 
                destination.write(chunk)
                destination.close()
            prev_urls.append(img_name)
    cache.imgs_urls = json.dumps(prev_urls)
    cache.save()
    content = {}
    content['response'] = json.loads(cache.imgs_urls)
    return HttpResponse(json.dumps(content), status=200, content_type="application/json")

@require_POST
def push_match_event(request):
    """
    Posts pictures to the model that inserts pictures into the text.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
       status code of this action.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    user = Profile.objects.get(user__id=identity)
    cache = user.cache
    imgs_urls = json.loads(cache.imgs_urls)
    if (len(imgs_urls) != 0):
        post_url = settings.SERVERB_TEXT_IMAGE_MATCH_URL
        text_array = cache.text
        file_data = []
        for i,name in enumerate(imgs_urls):
            path = os.path.abspath(settings.MEDIA_ROOT + '/img/imgs/' + name)
            # print(url)
            file_data.append(('files', ('file'+str(i), open(path,'rb'))))
        # print(file_data)
        data = {'text_array': text_array}
        res = requests.post(post_url, files=file_data, data=data )
        cache.match_list = str(json.loads(res.text)['order'])
        cache.save()
        # print(cache.match_list)
        content = {}
        content['response'] = json.loads(res.text)
        return HttpResponse(json.dumps(content), status=200, content_type="application/json")
    else:
        match_list = []
        cache.match_list = json.dumps(match_list)
        cache.save()
        return HttpResponse(json.dumps("ok"), status=200, content_type="application/json")

@require_POST
def post_text(request):
    """
    Posts text to the model that inserts pictures into the text.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of this action.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    post_body = json.loads(request.body.decode('utf-8'))
    user = Profile.objects.get(user__id=identity)
    cache = user.cache
    title = post_body['title']
    cache.title = title
    text_array = post_body['text'].split('\n')
    cache.text = json.dumps(text_array)
    cache.save()
    return HttpResponse(json.dumps(cache.text), status=200, content_type="application/json")

@require_POST
def post_confirmed_style(request):
    """
    Returns the result html string from the models that generate the initial typesetting.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        the result html from the models.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    # identity = 2
    post_body = json.loads(request.body.decode('utf-8'))
    styles = post_body['styles']

    user = Profile.objects.get(user__id=identity)
    cache = user.cache

    imgs_urls = json.loads(cache.imgs_urls)
    texts = json.loads(cache.text)
    match_list = json.loads(cache.match_list)
    title = cache.title

    # css_string = '<link href=\"'+ os.path.abspath("../media/css/test.css") + '\" type=\"text/css\" rel=\"stylesheet\"/>\n'

    body_string = "<div  id='write'  class = 'is-mac'>"

    if len(imgs_urls) != 0:
        body_string += "<h1>" + title + "</h1>"
        i = 0
        while i < len(texts):
            body_string += "<p>" + texts[i] + "</p>"
            for j in range(0,len(match_list)):
                if i == match_list[j]:
                    body_string += '<img src=\"http://202.120.40.109:19132/media/img/imgs/' + imgs_urls[j]  + '\" alt=\"' + imgs_urls[i] + '\" />'
            i = i + 1
    else:
        i = 0
        while i < len(texts):
            body_string += "<p>" + texts[i] + "</p>"
            i = i + 1
    body_string += "</div>"

    head_string = "<head>"
    head_string += '<meta charset="utf-8">'
    if (len(styles)==0):
        theme = Theme.objects.get(name="NONE")
    else:
        theme = Theme.objects.get(name=styles[0])
    style = theme.styles.all()[0]
    url = "https://github.com/Dianaaaa/temage_resources/blob/master/css/" + style.name + ".css"
    head_string  += "<link href=\""+ url +"\" rel=\"stylesheet\" type=\"text/css\" />"

    html_string = '<!DOCTYPE html><html>' + head_string + '<body>' + body_string + '</body></html>'
    
    content = {}
    content['html'] = html_string
    # print(html_string)
    return HttpResponse(json.dumps(content), content_type="application/json")

@require_POST
def store_passage(request):
    """
    Store the work information initially. 
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of this action.
    """
    token = request.META.get("HTTP_AUTHORIZATION")
    payload = jwt.decode(token, "Temage")
    identity = payload['id']
    post_body = json.loads(request.body.decode('utf-8'))
    user = Profile.objects.get(user__id=identity)
    cache = user.cache
    style_names = post_body['styles']
    html = post_body['res_html']
    title = post_body['title']
    width = post_body['t_width']
    score = 0

    product = Product.objects.create(title=title, html=html, creator=user, score=score, width=width)
    imgs_urls = json.loads(cache.imgs_urls)
    if (len(imgs_urls) != 0):
        path = os.path.abspath(settings.MEDIA_ROOT + '/img/imgs/' + imgs_urls[0])
        img = open(path, "rb")
        # print(">>>>>")
        # print(path)
        # print("<<<<<")
        product.image_src.save(imgs_urls[0], File(img), save=True)
    img_list = []
    cache.imgs_urls = json.dumps(img_list)
    cache.save()
    if (len(style_names) == 0):
        theme = Theme.objects.get(name="NONE")
        product.theme.add(theme)
    else:
        for name in style_names:
            # print(name)
            theme = Theme.objects.get(name=name)
            product.theme.add(theme)

    # store htmlfile
    file_name = "html_" + str(product.id) + ".html"
    product.html_file.save(file_name, ContentFile(html))

    content = {}
    content['ID'] = product.id
        
    # ES index create start
    index_data = {"title":title, "style":style_names, "ID": product.id}
    res = requests.post(settings.ES_CREATE_URL, 
                    headers = {'content-Type': 'application/json'},
                    data = json.dumps(index_data)
                )
    if res.status_code != 201:
        raise RuntimeError("The ES index has not been updated, please start ES server or check the post data")
        # ES index create end

    return HttpResponse(json.dumps(content), status = 200, content_type = "application/json")

@require_POST
def finished_work(request):
    """
    Previews the work after user's modifying.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        the url of html file generated finally.
        the width of this work.
    """
    post_body = json.loads(request.body.decode('utf-8'))
    product_id = post_body['productID']
    product = Product.objects.get(id=product_id)
    width = product.width
    url = product.html_file.url
    content = {}
    content['url'] = "http://202.120.40.109:19132/" + url
    content['width'] = width
    return HttpResponse(json.dumps(content), content_type = "application/json")

@require_POST
def download(request):
    """
    Download the image generated from the html file.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        the url of the image.
    """
    post_body = json.loads(request.body.decode('utf-8'))
    product_id = post_body['productID']

    # 生成pdf
    product = Product.objects.get(id=product_id)
    html_file = product.html_file.path 
    pdf_file_name = str(product_id) + ".pdf"
    pdf_file_path = settings.MEDIA_ROOT+'/pdf/' + pdf_file_name
    pdfkit.from_file(html_file, pdf_file_path)
    pdf_file = open(pdf_file_path, "rb")
    product.pdf_file.save(pdf_file_name, File(pdf_file), save=True)

    content = {}
    content['file_path'] = "http://202.120.40.109:19132/" + product.pdf_file.url

    response =FileResponse(pdf_file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="test.pdf"'
    return response

@require_POST
def confirm_store(request):
    """
    Stores the work finally.
    Parameters:
        request - this is a request to data from the front-end.
    Returns:
        status code of this action.
    """
    post_body = json.loads(request.body.decode('utf-8'))
    product_id = post_body['productID']
    stars = post_body['stars']
    vector = post_body['vector']
    try:
        product = Product.objects.get(id = product_id)
        product.is_finished = 1
        product.score = stars
        product.vector =  vector
        product.save()
        return HttpResponse(json.dumps("succeed"), status = 200, content_type = "application/json")
    except:
        return HttpResponse(json.dumps("error"), status = 400, content_type = "application/json")