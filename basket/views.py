from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from basket.basket_class import Basket
from mainApp.models import Good


def basket_page(request):
    return render(request, 'basket/basket_page.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'ADD':
        good_id = int(request.POST.get('goodid'))
        good_qty = int(request.POST.get('goodqty'))
        good = get_object_or_404(Good, id=good_id)

        basket.add(good=good, qty=good_qty)

    response = JsonResponse({'Sucsess': True})
    return response

