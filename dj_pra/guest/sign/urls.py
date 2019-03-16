# -*- coding: utf-8 -*-
# @Time       : 2019/3/6 15:27
# @Author     : Philly
# @File       : urls.py
# @Description:
from django.urls import path
from . import views
from sign import views_if


urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.login_action, name='login_action'),
    path('add_event/', views_if.add_event, name='add_event'),
    path('add_guest/', views_if.add_guest, name='add_guest'),
    path('get_event_list/', views_if.get_event_list, name='get_event_list'),
    path('get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
    path('user_sign/', views_if.user_sign, name='user_sign'),
]
