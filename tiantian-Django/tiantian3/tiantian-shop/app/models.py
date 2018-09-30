from django.db import models
from django.core import validators
import datetime


class User(models.Model):
    """用户信息"""
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    username = models.CharField(
        verbose_name='用户名', unique=True, max_length=30,
        validators=[validators.MinLengthValidator(limit_value=6, message='用户名不能少于6位')]
    )
    password = models.CharField(
        verbose_name='密码', max_length=30,
        validators=[
            validators.MinLengthValidator(limit_value=8, message='密码不能少于8位')
        ]
    )
    email = models.EmailField(
        verbose_name='邮箱', unique=True
    )

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=['username'])


class Category(models.Model):
    """分类信息"""
    name = models.CharField('名称', max_length=10, unique=True)
    icon = models.CharField('图片样式', max_length=20)


def upload_thumb(instance, filename):
    return '{0}_{1}.png'.format(
        instance.id, datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    )


class Goods(models.Model):
    """商品信息"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=30)
    price = models.DecimalField('价格', max_digits=5, decimal_places=2)
    thumb = models.ImageField('主图', upload_to=upload_thumb, null=True, blank=True)


class Cart(models.Model):
    """购物车"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods, through='CartGoods', through_fields=('cart', 'goods'))


class CartGoods(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    number = models.SmallIntegerField(default=0)
