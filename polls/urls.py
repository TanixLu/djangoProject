# coding=utf-8
# @Time : 2021/7/25 15:09
# @Author : Tanix Lu
# @File : urls.py
# @Software : PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
