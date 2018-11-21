import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *

# Create your views here.

def do_index(request):
    if 'tel' in request.session and 'uid' in request.session:
        uid = request.session.get('uid')
        user = Customers.objects.filter(id=uid)[0]
    return render(request, 'web/index.html', locals())

def do_register(request):
    if request.method == 'GET':
        return render(request, 'web/register.html')
    else:
        return HttpResponse('register done!')

def do_login(request):
    if request.method == 'GET':
        # 获取请求源地址  如果没有源地址则返回首页
        referer = request.META.get('HTTP_REFERER', '/')
        #将源地址存入cookies
        #判断tel  uid 是否同时存在session
        if 'tel' in request.session and 'uid' in request.session:
            return redirect(reverse('index'))
        else:
            #判断 tel  uid 是否同时存在COOKIES
            if 'tel' in request.COOKIES and 'uid' in request.COOKIES:
                tel = request.COOKIES.get('tel')
                uid = request.COOKIES
                request.session['tel'] = tel
                request.session['uid'] = uid
                return redirect(reverse('index'))
            else:
                cus = CusForm()  # 创建form表单实例
                #将源地址存入cookies
                resp = render(request, 'web/login.html', locals())
                resp.set_cookie('referer', referer)
                return resp
    else:
        tel = request.POST.get('tel')#得到提交的数据
        pwd = request.POST.get('pwd')
        user = Customers.objects.filter(tel = tel, pwd = pwd)#在数据库中查询手机号
        #从cookies中得到源地址
        referer = request.COOKIES.get('referer')
        resp = redirect(referer)
        #并将referer从cookies里面删除
        resp.delete_cookie('referer')
        if user:#手机号和密码正确，登录成功
            uid = user[0].id
            request.session['tel'] = tel#设置session
            request.session['uid'] = uid
            print(request.POST.get('isSave'))
            if request.POST.get('isSave'):#判断是否记住密码，记住则将tel, uid 保存进COOKIES
                resp.set_cookie('tel', tel, 60*60*24*365)
                resp.set_cookie('uid', uid, 60*60*24*365)
            return resp#返回源地址
        return redirect(reverse('login'))

def do_logout(request):
    return HttpResponse('logout done!')

def do_test(request):
    return render(request, 'ajax.html')

def do_ajax(request):
    dic = {"name":"jon", "age":34}
    data = json.dumps(dic)
    return HttpResponse(data)