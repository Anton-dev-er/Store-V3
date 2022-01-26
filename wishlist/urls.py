from django.urls import path

from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.WishlistPageView.as_view(), name='wishlist_page'),

    path('add/', views.WishlistAddView.as_view(), name='wishlist_add'),
    path('delete/', views.WishlistDeleteView.as_view(), name='wishlist_delete'),

]