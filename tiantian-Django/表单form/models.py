from django.db import models
from django.core import validators


class User(models.Model):
    """用户信息"""
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    username = models.CharField('用户名', unique=True, max_length=30,
                                validators=[
                                    validators.MinLengthValidator(limit_value=6,
                                                                  message='请输入6到20位用户名')])
    password = models.CharField('密码', max_length=30)
    email = models.EmailField('邮箱')
