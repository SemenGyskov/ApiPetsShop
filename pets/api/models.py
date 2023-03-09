from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

class Type(models.Model):
    type = models.CharField(max_length=20)

class Stat(models.Model):
    status = models.CharField(max_length=25)

class Pet(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=30)
    photo = models.ImageField()
    type = models.ManyToManyField(Type)
    status = models.ManyToManyField(Stat)

class Order(models.Model):
    pet = models.ManyToManyField(Pet)
    count = models.IntegerField()
    date_sell = models.DateField()
    status = models.ManyToManyField(Stat)
    sell = models.BooleanField()

