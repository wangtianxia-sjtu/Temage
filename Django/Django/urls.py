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

from django.conf.urls import url
from django.views.static import serve


explore_patterns = [
    path('', explore.get_homepage_data),
    path('gallery/', explore.get_gallery_data),
    path('gallery/more_cards/', explore.get_gallery_more_cards),
    path('collection/', explore.get_collection_data),
    path('get_recent/', explore.get_recent_data),
    path('product/', explore.get_product),
    path('post_collect/', explore.post_collect),
    path('delete/', explore.delete_product),
    path('cancel_collect/', explore.cancel_collect),
    path('post_search/', explore.post_search)
]



workflow_patterns = [
    path('post_picture/', workflow.post_picture),
    path('post_text/', workflow.post_text),
    path('push_match_event/', workflow.push_match_event),
    path('confirm_style/', workflow.post_confirmed_style),
    path('store_passage/', workflow.store_passage),
    path('finished_work/', workflow.finished_work),
    path('confirm_store/', workflow.confirm_store),
    path('download_picture/', workflow.download)
]

user_patterns = [
    path('register/', explore.post_register),
    path('login/', explore.post_login_submit),
    path('authenticate/', explore.post_jwt_authenticate),
]



api_patterns = [
    path('workflow/', include(workflow_patterns)),
    path('explore/', include(explore_patterns)),
    path('user/', include(user_patterns))
]


urlpatterns = [
    path('api/', include(api_patterns)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT})
]
