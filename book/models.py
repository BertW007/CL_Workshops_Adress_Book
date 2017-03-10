from django.db import models
from django.db.models.fields.related import ForeignKey

class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    description = models.TextField(null=True)
    address = models.ForeignKey('Address')
    
class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.IntegerField()

TYPE=((1,'home'),
      (2,'work'),
      (3,'other')
    )
    
class Telephone(models.Model):
    tel_number = models.CharField(max_length=16)
    type = models.IntegerField(choices=TYPE)
    person = ForeignKey(Person)
    
class Email(models.Model):
    email = models.EmailField()
    person = ForeignKey(Person)


    
    


