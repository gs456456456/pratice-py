# -*- coding: utf-8 -*-
from django import forms
from dairy import models

class Loginform(forms.Form):
    user_name = forms.CharField(label='你的姓名', max_length=10,widget=forms.TextInput(attrs={'placeholder':'请输入你的用户名'}))
    user_psd = forms.CharField(label='你的密码',widget=forms.PasswordInput(attrs = {'placeholder':'请输入你的密码'}))

class Registerform(forms.Form):
    user_name = forms.CharField(label='你的姓名', max_length=10,
                                error_messages={'required':'用户名不能为空'})
    psd = forms.CharField(label='你的密码',max_length=15,min_length=8,
                               widget=forms.PasswordInput(),
                               error_messages={'required':'密码不能为空','min_length':'密码最小长度8位'})
    psd2 = forms.CharField(label='请再次输入你的密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='你的邮件地址',widget=forms.TextInput)
    def clean(self):
        cleaned_data = self.cleaned_data
        pwd = self.cleaned_data['psd']
        pwd2 =self.cleaned_data['psd2']
        user_form = self.cleaned_data['user_name']
        user_model = list(models.User_info.objects.all().values_list('user_name'))
        for i in user_model:
            if user_form in i:
                raise forms.ValidationError('用户名已存在,请重新尝试登录')
        if pwd!=pwd2:
            raise forms.ValidationError('两次输入的密码不匹配')
        return cleaned_data

class DateInput(forms.DateInput):
    input_type = 'date'

class Dairyform(forms.ModelForm):
    class Meta:
        model = models.Dairy
        fields = ['budget','weight','note','ddate']
        widgets = {
            'ddate':DateInput()
        }
    def __init__(self,*args,**kwargs):
        super(Dairyform,self).__init__(*args,**kwargs)
        self.fields['budget'].label = '今日花费(元)'
        self.fields['weight'].label = '今日体重(kg)'
        self.fields['note'].label = '心情留言'
        self.fields['ddate'].label = '日期'





