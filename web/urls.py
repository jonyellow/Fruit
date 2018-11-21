from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', do_index, None, 'index'),
    url(r'^register/$', do_register, None, 'register'),
    url(r'^login/$', do_login, None, 'login'),
    url(r'^logout/$', do_logout, None, 'logout'),
    url(r'^ajax/$', do_ajax, None, 'ajax'),
    url(r'^test/$', do_test),
]