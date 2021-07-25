from django.db import models
# 内置的User模型
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ArticlePost(models.Model):
    # 作者，on_delete是删除方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    # 文章创建时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
