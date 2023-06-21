from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'), старый способ без классов
    path('login/', auth_views.LoginView.as_view(), name='login'), #вход в акк
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #выход с акка
    path('', views.dashboard, name='dashboard'), # вход в доску
]
