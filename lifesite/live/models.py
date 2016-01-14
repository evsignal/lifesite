from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
'''
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(default="something")

    def __str__(self):
        return self.name
'''

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()


class Article(models.Model):
    #blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=255, default="type your headline here")
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modification', default=timezone.now)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.headline
