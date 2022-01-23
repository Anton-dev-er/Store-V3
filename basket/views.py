from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from basket.basket_class import Basket
from mainApp.models import Good

import json


def basket_page(request):
    return render(request, 'basket/basket_page.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'ADD':
        good_id = int(request.POST.get('goodid'))
        good_qty = int(request.POST.get('goodqty'))
        good = get_object_or_404(Good, id=good_id)

        basket.add(good=good, qty=good_qty)

    basketqty = basket.__len__()
    response = JsonResponse({'qty': basketqty})

    return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'UPDATE':
        goods_data = request.POST.get('goods_data')
        basket.update(json.loads(goods_data))

        id_and_total_price = []

        for id_, value in basket.basket.items():
            id_and_total_price.append({id_: mul([int(i) for i in value.values()])})

        basketqty = basket.__len__()

        response = JsonResponse({'Ids and total prices': id_and_total_price,
                                 'total': basket.get_total_price(),
                                 'qty': basketqty, })
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'DELETE':
        good_id = request.POST.get('goodid')

        basket.delete(good_id=good_id)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})

        return response


def mul(lst):
    m = 1
    for i in lst:
        m = i * m
    return m
