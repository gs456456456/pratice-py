# -*- coding: utf-8 -*-
from ..models import Post,Category
from django import template

register = template.Library()
@register.simple_tag()#模版中通过PYTHON语法自定义函数
def get_recent_post(num=5):
    return Post.objects.all()[:num]
@register.simple_tag()
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')
@register.simple_tag()
def get_categories():
    return Category.objects.all()