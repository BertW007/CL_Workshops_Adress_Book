from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    description = models.TextField(null=True)
    address = models.ForeignKey('Address')
    
    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.IntegerField()
    
    def __str__(self):
        return '{} {}/{}'.format(self.city, self.street, self.house_number)

TYPE = ((1, 'home'),
        (2, 'work'),
        (3, 'other')
        )


class Telephone(models.Model):
    tel_number = models.CharField(max_length=16)
    type = models.IntegerField(choices=TYPE)
    person = models.ForeignKey(Person)
    
    def __str__(self):
        return '{} {}'.format(self.tel_number, self.get_type_display())


class Email(models.Model):
    email = models.EmailField()
    person = models.ForeignKey(Person)
    
    def __str__(self):
        return '{}'.format(self.email)
