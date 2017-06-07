# -*- encoding: utf-8 -*-
from django import forms
from mysite import models
from django.forms import ModelForm
# from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    CITY = [
        ['CH', 'China'],
        ['JP', 'Japan'],
    ]
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在学', required=False)
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='您的意见', widget=forms.Textarea)
    
class PostForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_psd']
        labels = {
            'mood':'现在心情',
            'nickname':'你的昵称',
            'message':'心情留言',
            'del_psd':'设置密码',
        }



