# coding=utf-8
# @Time : 2021/7/25 22:57
# @Author : Tanix Lu
# @File : urls.py
# @Software : PyCharm

from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article_create/', views.article_create, name='article_create'),
    path('article_safe_delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
]
