from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
