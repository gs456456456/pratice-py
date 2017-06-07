# -*- coding: utf-8 -*-
from django.http import HttpResponse
from dairy import models, forms
from django.shortcuts import redirect,render



def login(request):
    if request.method=='POST':
        login_form = forms.Loginform(request.POST)
        if login_form.is_valid():
            login_name = request.POST['user_name']
            login_psd = request.POST['user_psd']
            try:
                user = models.User_info.objects.get(user_name=login_name)
                if user.psd == login_psd:
                    request.session['username'] =login_name
                    request.session['psd'] = login_psd
                    request.session['login'] = True
                    message = '恭喜成功登录'
                    return redirect('dairy:login_after')
                else:
                    message ='密码错误'
            except:
                message ='找不到用户'
        else:
            message ='请检查你输入的字段内容'
    else:
        login_form = forms.Loginform()
    return render(request,'login.html',locals())

def login_after(request):
    if request.session.get('login',None):
       username = request.session.get('username')
       return render(request,'login_after.html',locals())
    else:
        return redirect('dairy:login')

def logout(request):
    request.session.clear()
    return redirect('dairy:login')

def register(request):
    if request.method == 'POST':
        register_form = forms.Registerform(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            models.User_info.objects.create(**data)
            message = '您已注册成功,请继续操作'
            return render(request,'register.html',locals())
        else:
            message='请稍后注册'
            return render(request,'register.html',locals())
    else:
        register_form = forms.Registerform()
    return render(request,'register.html',locals())


def daily(request):
    if request.method == 'POST':
        user_name = request.session.get('username')
        user_name_user = models.User_info.objects.get(user_name=user_name)
        daily = models.Dairy(user = user_name_user)
        daily_form = forms.Dairyform(request.POST,instance=daily)
        if daily_form.is_valid():
            daily_form.save()
            return redirect('dairy:list')
        else:
            message = '请正确填入每个字段'
            return render(request,'daily.html',locals())
    else:
        daily_form = forms.Dairyform()
        return render(request,'daily.html',locals())

def list2(request):
    posts = models.Dairy.objects.order_by('ddate')[:150]
    for x in posts:
        print(x)
    return render(request,'list2.html',locals())


# Create your views here.
