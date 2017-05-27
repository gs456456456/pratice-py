# -*- encoding: utf8 -*-
from django.db import models

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default='unknown')
    message = models.TextField(null=False)
    del_psd = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    def __str__(self):
        return self.message

