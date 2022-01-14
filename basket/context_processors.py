from .basket_class import Basket


def basket(request):
    return {'basket': Basket(request)}