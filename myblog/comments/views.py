# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render,get_object_or_404,redirect
from django import forms
from . import models
from .models import comment
from blog.models import Post
from django.http import HttpResponse

class Commentmodelform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name','email','url','text']
        error_messages = {
            'name':{
                'required':'用户名不能为空'
            },
            'email':{
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误..',
            }
        }

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'名字'}),
            'email': forms.TextInput(attrs={'placeholder':'email'}),
            'url' : forms.TextInput(attrs={'placeholder':'url'}),
            'text' : forms.Textarea(attrs={'placeholder':'评论内容'}),

        }

def comments(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    form = Commentmodelform(request.POST)
    if request.method == "GET":
        comment_list = post.comment_set.all()
        return render(request,'blog/detail.html',{'post':post,'form':form,'comment_list':comment_list})
    elif request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            print(comment)
            comment.post = post
            comment.save()
            # return redirect(post)
            return redirect(reverse('blog:detail',kwargs={'pkq':post_pk}))
        else:
            return HttpResponse('您的填写信息有误')
    else:
        # return redirect(post)
        return redirect(reverse('blog:detail',kwargs={'pkq':post_pk}))
    





# Create your views here.
