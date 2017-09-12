from book.models import Address, Email, Person, Telephone
from django.contrib import admin

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Telephone)
admin.site.register(Email)
