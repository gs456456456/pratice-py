# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog import models
from django.shortcuts import render,get_object_or_404
from .models import Post
from comments.views import Commentmodelform

def index(request):
    return render(request, 'blog/index.html', context={
                      'title': '我的博客首页',
                      'welcome': '欢迎访问我的博客首页'
                  })

def index(request):
    post_list = models.Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})
# Create your views here.


def detail(request, pkq):
    post_1 = models.Post.objects.all()
    post = get_object_or_404(Post,pk =pkq)
    import markdown

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = Commentmodelform()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'blog/detail.html', context=context)

def achieve(request,year,month):
    post_list = models.Post.objects.filter(created_time__year=year,created_time__month=month)
    print(post_list)
    return render(request,'blog/index.html',context={'post_list':post_list})

def catagory(request,catalog):
    cate = get_object_or_404(models.Category, pk=catalog)
    post_list =models.Post.objects.filter(category = cate)
    return render(request,'blog/index.html',context={'post_list':post_list})
