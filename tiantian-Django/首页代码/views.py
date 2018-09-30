from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import User, Category, Goods


def index(request):
    """首页"""
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'user': request.session.get('user')
    })


def register(request):
    """用户注册处理"""
    if request.method == 'POST':
        # 获取用户注册表单中提交的数据
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        # 正则验证数据
        # 使用模型类添加用户
        user = User.objects.create(username=username,
                                   password=password1,
                                   email=email)
        if user is not None:
            return HttpResponse('注册成功')
        else:
            return HttpResponse('注册失败')
    else:
        return render(request, 'register.html')


def login(request):
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


# def login(request):
#     """登录处理"""
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(username=username, password=password)
#         except Exception:
#             return HttpResponse('账号密码不对')
#         return HttpResponse('登录成功')
#     else:
#         return render(request, 'login.html')


def test(request):
    if request.method == 'POST':
        # name = request.POST.get('your-name')
        # return HttpResponse(name)
        form = TestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = TestForm()
    return render(request, 'test.html', {'form': form})
