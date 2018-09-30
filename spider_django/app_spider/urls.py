from django.urls import path
from . import views

urlpatterns=[

    path('find/',views.find,name='find'),
    path('find2/',views.find2,name='find2'),
    path('find3/',views.find3,name='find3'),
    path('find4/',views.find4,name='find4'),
    path('find5/',views.find5,name='find5'),
]