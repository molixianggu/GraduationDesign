"""GraduationDesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from managementSystem.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name = 'home'),
    url(r'Console', Console, name = 'Console'), 
    url(r'getPage', getPage, name = 'getPage'), 
    url(r'addUser', addUser, name = 'addUser'),
    url(r'delUser', delUser, name = 'delUser'),
    url(r'preview', preview, name='preview'),
    url(r'changeJuris', changeJuris, name='changeJuris'),
    url(r'delReport', delReport, name='delReport'),
    url(r'outputReport', outputReport, name='outputReport'),
]
