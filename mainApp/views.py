from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Category, Good


class HomeView(View):
    template_name = 'mainApp/home.html'

    def get(self, request, *args, **kwargs):
        filter_value = request.GET.get('filter')
        if filter_value == 'by-date':
            ordered_goods = Good.objects.order_by('-created_dt')[:8]
        elif filter_value == 'by-views':
            ordered_goods = Good.objects.order_by('-views')[:8]
        elif filter_value == 'by-price':
            ordered_goods = Good.objects.order_by('price')[:8]
        else:
            ordered_goods = Good.objects.all()[:8]

        context = {
            "all_goods": ordered_goods
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        pass


class CatalogListView(ListView):
    template_name = 'mainApp/catalog_gender.html'
    context_object_name = 'categories_sex'
    queryset = Category.objects.filter(level=0)


class CategoryByGenderView(View):
    template_name = 'mainApp/goods_by_categories.html'

    def get(self, request, *args, **kwargs):
        slug_gender = self.kwargs['slug']
        categories = Category.objects.get(slug=slug_gender).get_descendants(include_self=False)
        goods = []
        for cat in categories:
            if cat.is_published:
                goods.extend(cat.good_set.filter(is_published=True))

        context = {
            'categories': categories,
            'slug_gender': slug_gender,
            'categories_gender': Category.objects.filter(level=0),
            'goods': goods
        }
        return render(request, self.template_name, context=context)


class GoodByCategoryView(View):
    template_name = 'mainApp/goods_by_categories.html'

    def get(self, request, *args, **kwargs):
        slug_gender = self.kwargs['slug_gender']
        goods = Good.objects.filter(category__slug=self.kwargs['slug_category'], is_published=True)
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

    def dispatch(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        good = Good.objects.get(slug=slug)
        good.views = good.views + 1
        good.save()
        return super(GoodDetailView, self).dispatch(request, args, kwargs)

