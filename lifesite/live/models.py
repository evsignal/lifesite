from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Article(models.Model):
    title_text = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text



