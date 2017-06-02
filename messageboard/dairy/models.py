# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User_info(models.Model):
    user_name = models.CharField(max_length=10)
    psd = models.CharField(max_length=15)
    psd2 = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.user_name

class Dairy(models.Model):
    user = models.ForeignKey(to=User_info,on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateField()
    def __str__(self):
        return '{0},{1}'.format(self.ddate,self.user)

# Create your models here.
