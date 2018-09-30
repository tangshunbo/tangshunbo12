from django.contrib import admin
from .models import User, Category, Goods

admin.site.register([User, Category, Goods])
