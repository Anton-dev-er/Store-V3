from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('catalog', views.CatalogListView.as_view(), name='catalog'),
    path('catalog/<slug:slug>', views.CategoryByGenderView.as_view(), name='catalog_sex'),
    path('catalog/<slug:slug_gender>/<slug:slug_category>', views.GoodByCategoryView.as_view(), name='good_by_category'),

    path('good/<slug:slug>', views.GoodDetailView.as_view(), name='good_detail'),
]
