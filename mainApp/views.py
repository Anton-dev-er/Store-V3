from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Category, Good


class HomeView(View):
    template_name = 'mainApp/home.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context=context)


class CatalogListView(ListView):
    template_name = 'mainApp/catalog_gender.html'
    context_object_name = 'categories_sex'
    queryset = Category.objects.filter(level=0)


class CategoryByGenderView(View):
    template_name = 'mainApp/goods_by_categories.html'

    def get(self, request, *args, **kwargs):
        slug_gender = self.kwargs['slug']

        context = {
            'categories': Category.objects.get(
                slug=slug_gender
            ).get_descendants(include_self=False),
            'slug_gender': slug_gender,
            'categories_gender': Category.objects.filter(level=0),
        }
        return render(request, self.template_name, context=context)


class GoodByCategoryView(ListView):
    template_name = 'mainApp/goods_by_categories.html'

    def get(self, request, *args, **kwargs):
        slug_gender = self.kwargs['slug_gender']
        goods = Good.objects.filter(category__slug=self.kwargs['slug_category'])
        categories = Category.objects.get(slug=slug_gender).get_descendants(include_self=False)
        Genders = Category.objects.filter(level=0)

        context = {
            'categories': categories,
            'slug_gender': slug_gender,
            'categories_gender': Genders,
            'goods': goods
        }

        return render(request, self.template_name, context=context)


class GoodDetailView(DetailView):
    template_name = 'mainApp/good_detail.html'
    model = Good

