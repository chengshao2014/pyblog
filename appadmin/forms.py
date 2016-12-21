#-*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
class BlogForm(forms.Form):
    title = forms.CharField(label = '标题')
    body = forms.CharField(label = '内容',widget=forms.Textarea)
    status = forms.CharField(label = '作者')

class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()