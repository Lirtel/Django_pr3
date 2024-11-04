# myproject/urls.py
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('page/', views.page, name='page'),
    path('register/', views.register, name='register'),  # Новый путь для регистрации
]
