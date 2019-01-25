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

api_patterns = [
    path('', views.get_homepage_data),
    path('work/<int:work_id>', views.get_work_data),
    path('gallery', views.get_gallery_data),
    path('gallery/more_cards', views.get_gallery_more_cards),
    path('collection', views.get_collection_data),
    path('recent', views.get_rescent_data),
    path('text', views.get_text),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
    path('register', views.register),
    path('login/submit/', views.login_submit),
    path('authenticate', views.JWTauthenticate),

    # for quick model test
    path('test/', views.test),
]
