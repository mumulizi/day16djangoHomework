#! _*_ conding:utf-8 _*_
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30,unique=True)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


    # def __unicode__(self):
    def __str__(self):
        return "<%s>" %(self.name)

class Authon(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return "<%s %s>" %(self.first_name,self.last_name)

class Book(models.Model):
    name = models.CharField(max_length=128)
    authors = models.ManyToManyField(Authon)
    publisher = models.ForeignKey(Publisher)
    publish_date = models.DateField()
    def __str__(self):
        return "<%s>" %(self.name)