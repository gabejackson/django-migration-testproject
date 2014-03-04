from django.db import models

class DeliveryCountry(models.Model):
    country = models.CharField(max_length=255)

class Package(models.Model):
    delivery_person = models.ForeignKey('a.ShopUserPerson')
    delivery_address = models.ForeignKey('a.ShopUserAddress')
    delivery_contact = models.ForeignKey('a.ShopUserContact')