#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: yu
# @Date  : 2019/10/16
from django.conf.urls import url
from stockInfo import views

urlpatterns = [
    url(r'^addList$',views.addList),
    url(r'^test$', views.test),
    url(r'^$', views.home),
]