# coding=utf-8
# @Time : 2021/7/25 23:54
# @Author : Tanix Lu
# @File : forms.py
# @Software : PyCharm
# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost


# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')
