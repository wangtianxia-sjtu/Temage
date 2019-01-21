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
    url(r'^$', views.get_homepage_data),
    url(r'^work/(.[0-9]+)$', views.get_work_data),
    url(r'^gallery$', views.get_gallery_data),
    url(r'^gallery/more_cards', views.get_gallery_more_cards),
    url(r'^collection$', views.get_collection_data),
    url(r'^recent$', views.get_rescent_data),
    url(r'^text$', views.get_text),
]


urlpatterns = [
    url(r'user/(.+)/', views.get_user),
    url(r'^admin/', admin.site.urls),
    url('api/', include(api_patterns)),
    # url(r'^api/work/(.[0-9]+)$', views.get_work_data),
    # url(r'^api/gallery$', views.get_gallery_data),
    # url(r'^api/gallery/more_cards', views.get_gallery_more_cards),
    # url(r'^api/collection$', views.get_collection_data),
    # url(r'^api/recent$', views.get_rescent_data),
    # url(r'^api/text$', views.get_text),
    url(r'^register', views.register),
    url(r'^login/submit', views.login_submit),
    url(r'^authenticate', views.JWTauthenticate),

    # for quick model test
    url(r'^test', views.test),
]
