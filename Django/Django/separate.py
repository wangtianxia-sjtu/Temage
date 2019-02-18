"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Temage import views
from django.conf.urls import url

index_patterns = [
    path('', views.get_homepage_data),
    path('gallery', views.get_gallery_data),
    path('gallery/more_cards', views.get_gallery_more_cards),
    path('collection', views.get_collection_data),
    path('recent', views.get_rescent_data),
]
work_patterns = [
    path('download', views.download),
    path('<int:work_id>', views.get_work_data),
    path('text', views.get_text),
    path('destroy', views.destroy),
]
workflow_patterns = [
    path('pic_post', views.pic_post),
    path('text_post', views.text_post),
    path('ret_html', views.ret_html),
    path('store_passage', views.store_passage),
    path('finished_work', views.finished_work),
    path('confirm_store', views.confirm_store),
]

user_patterns = [
    path('register', views.register),
    path('login/submit/', views.login_submit),
    path('authenticate', views.JWTauthenticate),
]
api_patterns = [
    # indclude all of before
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),

    # for quick model test
    path('test/', views.test),
]
