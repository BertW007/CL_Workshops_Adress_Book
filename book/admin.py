from django.contrib import admin
from book.models import Person,Address,Telephone,Email

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Telephone)
admin.site.register(Email)
