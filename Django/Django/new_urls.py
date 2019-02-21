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
from django.urls import path, include
from  .views import *
from django.conf.urls import url


explore_patterns = [
    path('', explore.homepage_data),
    path('gallery/', explore.gallery_data),
    path('gallery/more_cards/', explore.gallery_more_cards),
    path('collection/', explore.collection_data),
    path('recent/', explore.recent_data),
    path('text/', explore.text),
    path('collect/', explore.collect),
    path('delete/', explore.delete_product),
    path('cancel_collect/', explore.cancel_collect),
    path('post_search/', explore.post_search)
]



workflow_patterns = [
    path('pic_post/', workflow.pic_post),
    path('text_post/', workflow.text_post),
    path('ret_html/', workflow.ret_html),
    path('store_passage/', workflow.store_passage),
    path('finished_work/', workflow.finished_work),
    path('confirm_store/', workflow.confirm_store),
    path('download/', workflow.download)
]

user_patterns = [
    path('register/', explore.register),
    path('login/submit/', explore.login_submit),
    path('authenticate/', explore.JWTauthenticate),
]



api_patterns = [
    path('workflow/', include(workflow_patterns)),
    path('explore/', include(explore_patterns)),
    path('user/', include(user_patterns))
]


urlpatterns = [
    path('api/', include(api_patterns))
]
