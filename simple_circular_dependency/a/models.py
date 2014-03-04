from django.conf import settings
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)

class ShopUserPerson(Person):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='persons')
    archived = models.BooleanField(default=False, editable=False)

class Contact(models.Model):
    email = models.EmailField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)

class ShopUserContact(Contact):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contacts')

class Address(models.Model):
    country = models.ForeignKey('b.DeliveryCountry')
    date_added  = models.DateTimeField(auto_now_add=True, editable=False)

class ShopUserAddress(Address):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='addresses')
    archived = models.BooleanField(default=False, editable=False)