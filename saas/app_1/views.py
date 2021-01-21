from app_1 import models
# from redis import *
from django.shortcuts import render, HttpResponse
from random import *
from django.core.validators import RegexValidator
from django.conf import settings
from utils.tencent.sms import send_sms_single
from django import forms
from django_redis import get_redis_connection


# POOL = ConnectionPool(host='127.0.0.1', port=6379, password='foobared', encode='utf-8',max_connections=1000)


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机格式不正确'), ])
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '请输入重复密码'}))
    code = forms.CharField(label='验证码',
                           widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入验证码'}))


    class Meta:
        model = models.Userinfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f"请输入{field.label}"


def send_single(request):
    tpl = request.GET.get('tpl')
    tpl_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    print(tpl, tpl_id)
    if not tpl_id:
        return HttpResponse('模板不存在')
    code = randrange(1000, 9999)
    res = send_sms_single('18231346616', 549888, [code, ])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])


def register(request):
    form = RegisterModelForm()
    password = request.POST.get('password')
    re_pwd = request.POST.get('confirm_password')
    return render(request, 'app_1/register.html', locals())
