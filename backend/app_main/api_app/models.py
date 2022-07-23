from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    phone = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    zip_code = models.CharField(max_length=64, null=True)
    address1 = models.TextField(null=True)
    address2 = models.TextField(null=True)
    is_admin = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64,null=True)
    website = models.CharField(max_length=64,null=True)
    address = models.TextField(blank = True)