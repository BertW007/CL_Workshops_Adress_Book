"""Address_Book URL Configuration

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
from book.views import AddPerson, ModifyPerson, AllPersons, delete_person, person_details
from book.views import AddEmail, EditEmail, delete_email, AddTelephone, EditTelephone, delete_telephone

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new/$', AddPerson.as_view()),
    url(r'^all_persons/$', AllPersons.as_view()),
    url(r'^modify/(?P<person_id>\d+)$', ModifyPerson.as_view()),
    url(r'^delete_person/(?P<person_id>\d+)$', delete_person),
    url(r'^person_details/(?P<person_id>\d+)$', person_details),
    url(r'^edit_email/(?P<person_id>\d+)/(?P<email_id>\d+)$', EditEmail.as_view()),
    url(r'^delete_email/(?P<person_id>\d+)/(?P<email_id>\d+)$', delete_email),
    url(r'^add_email/(?P<person_id>\d+)$', AddEmail.as_view()),
    url(r'^edit_telephone/(?P<person_id>\d+)/(?P<telephone_id>\d+)$', EditTelephone.as_view()),
    url(r'^delete_telephone/(?P<person_id>\d+)/(?P<telephone_id>\d+)$', delete_telephone),
    url(r'^add_telephone/(?P<person_id>\d+)$', AddTelephone.as_view()),
]
