from mainApp.models import Good


class Basket:

    def __init__(self, request):

        self.session = request.session
        basket = self.session.get('Basket items')
        if 'Basket items' not in request.session:
            basket = self.session['Basket items'] = {}
        self.basket = basket

    def add(self, good, qty):
        good_id = str(good.pk)

        if good_id in self.basket:
            self.basket[good_id]['qty'] = int(self.basket[good_id]['qty']) + qty
            print(type(qty))
        else:
            self.basket[good_id] = {'price': str(good.price), 'qty': qty}
        self.save()

    def update(self, new_goods_data):
        good_ids = self.basket.keys()

        for key, value in new_goods_data.items():
            if key in good_ids:
                self.basket[key]['qty'] = int(value['qty'])

        self.save()

    def delete(self, good_id):
        if good_id in self.basket:
            del self.basket[good_id]

        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        good_ids = self.basket.keys()
        goods = Good.objects.filter(id__in=good_ids)
        basket = self.basket.copy()

        for good in goods:
            basket[str(good.id)]['good'] = good

        for item in basket.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
