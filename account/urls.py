from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('register/', views.account_register, name='register'),
    path('login/', views.account_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
]