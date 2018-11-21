import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *

# Create your views here.

def do_index(request):
    return render(request, 'web/index.html')

def do_register(request):
    if request.method == 'GET':
        regCu = RegForm()
        return render(request, 'web/register.html', locals())
    else:
        return HttpResponse('register done!')
def do_check_register(request):
    tel = request.GET.get('tel')
    user = Customers.objects.filter(tel=tel)
    msg = {'status': 0, 'msg': '手机号正确！'}
    if user:
        msg['status'] = 1
        msg['msg'] = '手机号已存在！'
    return HttpResponse(json.dumps(msg))

def do_login(request):
    if request.method == 'GET':
        # 获取请求源地址  如果没有源地址则返回首页
        referer = request.META.get('HTTP_REFERER', '/')
        #将源地址存入cookies
        #判断tel  uid 是否同时存在session
        if 'tel' in request.session and 'uid' in request.session:
            print(request.session.get('uid'))
            return redirect(reverse('index'))
        elif 'tel' in request.COOKIES and 'uid' in request.COOKIES:
            #判断 tel  uid 是否同时存在COOKIES
            tel = request.COOKIES.get('tel')
            uid = request.COOKIES.get('uid')
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
            if request.POST.get('isSave'):#判断是否记住密码，记住则将tel, uid 保存进COOKIES
                resp.set_cookie('tel', tel, 60*60*24*365)
                resp.set_cookie('uid', uid, 60*60*24*365)
            return resp#返回源地址
        return redirect(reverse('login'))

def do_logout(request):
    url = request.META.get('HTTP_REFERER', '/')
    resp = redirect(url)
    #如果session中存在，则删除session
    if 'uid' in request.session and 'tel' in request.session:
        del request.session['uid']
        del request.session['tel']
        return resp
    # 如果session中不存在，而COOKIES中存在，则删除COOKIES
    elif 'uid' in request.COOKIES and 'tel' in request.COOKIES:
        resp.delete_cookie('uid')
        resp.delete_cookie('tel')
        return resp
    return redirect(reverse('index'))

def do_loginstatus(request):
    data = {"status": 0}
    data['logout'] = reverse('logout')
    data['login'] = reverse('login')
    data['register'] = reverse('register')
    #用于验证用户是否登录成功，以便在导航栏显示登录信息,返回登录的用户名和退出的url
    if 'tel' in request.session and 'uid' in request.session:
        uid = request.session.get('uid')#session中存在则是登录状态
        user = Customers.objects.filter(id=uid)[0]
        data['name'] = user.name
        data['status'] = 1
    else:
        if 'tel' in request.COOKIES and 'uid' in request.COOKIES:
            uid = request.COOKIES.get('uid')#在COOKIES中存在则是登录状态。
            user = Customers.objects.filter(id=uid)[0]
            data['name'] = user.name
            data['status'] = 1
    return HttpResponse(json.dumps(data))

def do_load_goodsType(request):
    all_list = []
    #读取GoodsType下的所有内容,{'type':xxx, 'goods':{}}
    types = GoodsType.objects.all()
    for type in types:
        typejson = json.dumps(type.to_dict())
        goods = type.goods_set.all()[:10]
        dic = {
            'type': typejson,
        }
        goodjson = serializers.serialize(goods)
        dic['goods'] = goodjson
        all_list.append(dic)
    return HttpResponse(json.dumps(all_list))