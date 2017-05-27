# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post',to_field='id')
    def __str__(self):
        return self.text[:20]

# Create your models here.
