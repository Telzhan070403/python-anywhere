from random import randint

from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Названия', max_length=80)
    news = models.TextField('Описания', blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


class SummerSport(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    gold = models.IntegerField()
    silver = models.IntegerField()
    bronze = models.IntegerField()
    overall = models.IntegerField()

    def __str__(self):
        return self.name


class WinterSport(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    gold = models.IntegerField()
    silver = models.IntegerField()
    bronze = models.IntegerField()
    overall = models.IntegerField()

    def __str__(self):
        return self.name


#
# class User(models.Model):
#     login = models.CharField(max_length=50)
#     last = models.CharField(max_length=50)
#     firs = models.CharField(max_length=50)
#     number = models.IntegerField()
#     city = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     password1 = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.login


class Registration(models.Model):
    name = models.CharField(max_length=15, )
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    email = models.EmailField(blank=True, unique=True)
    telnumber = models.IntegerField(max_length=11, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'
        ordering = ['name', 'lastname']

