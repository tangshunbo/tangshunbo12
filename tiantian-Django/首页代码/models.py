from django.db import models
from django.core import validators


class User(models.Model):
    """用户信息"""
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    username = models.CharField(
        '用户名', unique=True, max_length=30,
        validators=[validators.MinLengthValidator(limit_value=6, message='请输入6到20位用户名')]
    )
    password = models.CharField(verbose_name='密码', max_length=30)
    email = models.EmailField('邮箱')

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=['username'])


class Category(models.Model):
    """分类信息"""
    name = models.CharField('名称', max_length=10, unique=True)
    icon = models.CharField('图片样式', max_length=20)


class Goods(models.Model):
    """商品信息"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=30)
    price = models.DecimalField('价格', max_digits=5, decimal_places=2)
    picture = models.ImageField('主图', null=True, blank=True)
