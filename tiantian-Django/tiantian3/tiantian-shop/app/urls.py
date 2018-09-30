from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.goods_list, name='list'),
    path('detail/<int:goods_id>/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]