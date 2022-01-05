from django.urls import path
from oauth.views import auth_views

urlpatterns = [
    path('google/', auth_views.google_auth),
    path('', auth_views.google_login),
]
