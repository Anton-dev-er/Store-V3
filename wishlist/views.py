from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from mainApp.models import Good
from wishlist.models import Wishlist


class WishlistPageView(View):
    template_name = 'wishlist/wishlist_page.html'

    def get(self, request):
        context = {
            'items': Wishlist.objects.filter(user=request.user)
        }
        return render(request, self.template_name, context=context)


class WishlistAddView(View):
    def post(self, request):
        if request.POST.get('action') == 'ADD':
            if request.user.is_authenticated:
                wished_item, created = Wishlist.objects.get_or_create(good=Good.objects.get(pk=request.POST.get('goodid')),
                                                                      user=request.user, )

                if not created:
                    wished_item.delete()

                response = JsonResponse({'is_authenticated': True})
            else:
                response = JsonResponse({'is_authenticated': False})

            return response


class WishlistDeleteView(View):
    def post(self, request):
        if request.POST.get('action') == 'DELETE':
            Wishlist.objects.get(good=Good.objects.get(pk=request.POST.get('goodid')), user=request.user).delete()

            return JsonResponse({'items': "OK"})
