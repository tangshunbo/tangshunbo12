from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from .models import User, Category, Goods
import math

def index(request):
    """首页"""
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'user': request.session.get('user')
    })


def goods_list(request):
    """商品列表页面"""
    # 获取get请求传递低参数
    category_id = request.GET.get('category_id')
    # 从页面获取当前点击的页码（转成整数类型）
    page = int(request.GET.get('page', 1))
    is_first = True
    if page !=  1:
        is_first = False
    # 获取当前分类下的所有商品
    goods = Category.objects.get(pk=category_id).goods_set.all()
    # 计算总页码
    pages = range(1, math.ceil(goods.count() / 1) + 1)
    return render(request, 'list.html', {
        'category_id': category_id,
        'goods': goods[(page-1)*1:(page-1)*1+1],
        'pages': pages,
        'is_first': is_first
    })

def register(request):
    """用户注册处理"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(data)
            if user is not None:
                return HttpResponse('注册成功')
            else:
                return HttpResponse('注册失败')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    """用户登录处理"""
    if request.method == 'POST':
        # 用表单提交过来的数据创建一个LoginForm对象
        form = LoginForm(request.POST)
        # 判断表单数据是否合法
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = User.objects.get(username=data['username'], password=data['password'])
            except Exception:
                return HttpResponse('用户名密码错误')
            # 登录成功, 需要将当前登录的用户保存记录下来(使用session存储数据，可以在服务端进行全局共享)
            request.session['user'] = user.serializable_value('username')
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
