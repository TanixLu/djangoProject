# coding=utf-8
# @Time : 2021/7/25 22:57
# @Author : Tanix Lu
# @File : urls.py
# @Software : PyCharm

from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    path('article-update/<int:id>/', views.article_update, name='article_update')
]
