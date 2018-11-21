from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', do_index, None, 'index'),
    url(r'^register/$', do_register, None, 'register'),
    url(r'^login/$', do_login, None, 'login'),
    url(r'^logout/$', do_logout, None, 'logout'),
    url(r'^loginstatus/$', do_loginstatus, None, 'loginstatus'),
    url(r'^checkregister', do_check_register, None, 'checkregister'),
    url(r'^goods_type/$', do_load_goodsType, None, 'goods_type')
]