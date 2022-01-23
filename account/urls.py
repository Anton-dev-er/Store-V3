from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views
from .forms import PwdResetForm, PwdResetConfirmForm

app_name = 'account'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('register/', views.account_register, name='register'),
    path('login/', views.account_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),

    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    # Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="account/user/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='account/user/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),

    path('password_reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',
                                                     success_url='password_reset_complete/',
                                                     form_class=PwdResetConfirmForm),
         name="password_reset_confirm"),

    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_done'),

    path('password_reset_confirm/Mg/password_reset_complete/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_complete'),

]
