"""Addres_Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from book.views import AddPerson,ModifyPerson,all_persons,delete_person,person_details

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new/$', AddPerson.as_view()),
    url(r'^all_persons/$', all_persons),
    url(r'^modify/(?P<person_id>\d+)$', ModifyPerson.as_view()),
    url(r'^delete_person/(?P<person_id>\d+)$', delete_person),
    url(r'^person_details/(?P<person_id>\d+)$', person_details),
]
