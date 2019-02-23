#-*-coding:utf-8-*-
"""Django URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from  .views import *

from django.urls import path
from django.urls import include

from Temage import views
from django.conf.urls import url


explore_patterns = [
    path(r'', explore.get_homepage_data),
    path(r'gallery/', explore.get_gallery_data),
    path(r'gallery/more_cards/', explore.get_gallery_more_cards),
    path(r'collection/', explore.get_collection_data),
    path(r'recent/', explore.get_recent_data),
    path(r'product/<int:product_id>', explore.get_product),
    path(r'post_collect/', explore.post_collect),
    path(r'delete/', explore.delete_product),
    path(r'cancel_collect/', explore.cancel_collect),
    path(r'post_search/', explore.post_search)
]



workflow_patterns = [
    path(r'post_picture/', workflow.post_picture),
    path(r'text_post/', workflow.post_text),
    path(r'confirm_style/', workflow.post_confirmed_style),
    path(r'store_passage/', workflow.store_passage),
    path(r'finished_work/', workflow.finished_work),
    path(r'confirm_store/', workflow.confirm_store),
    path(r'download/', workflow.download)
]

user_patterns = [
    path(r'register/', explore.post_register),
    path(r'login/submit/', explore.post_login_submit),
    path(r'authenticate/', explore.post_jwt_authenticate),
]



api_patterns = [
    path('workflow/', include(workflow_patterns)),
    path(r'explore/', include(explore_patterns)),
    path(r'user/', include(user_patterns))
]


urlpatterns = [
    path('api/', include(api_patterns))
]
