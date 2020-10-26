from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 创建分类表
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 创建标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 创建文章表
class Post(models.Model):
    # 文章标题
    titel = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 最后一次修改的时间
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 外键
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签 多对多
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.titel
