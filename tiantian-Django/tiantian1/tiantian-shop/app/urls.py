from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.goods_list, name='list'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]