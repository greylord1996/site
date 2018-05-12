"""
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""

from django.db import models

CATEGORIES = ((1, "Метлы"), (2, "Швабры"), (3, "Веники"))

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name




class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    description = models.TextField()
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="В наличии")
    add_from_administration = models.BooleanField(default=False, db_index=True, verbose_name="Из админки")
    #category = models.IntegerField(choices=CATEGORIES, default=1, db_index=True)
    category = models.ForeignKey(Category, null=True, blank=True, db_index=True, on_delete=models.SET_NULL)
    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + "нет в наличии"
        return s




