from django.db import models as m

from application_settings import settings
from mainApp.models import Good


class Wishlist(m.Model):
    user = m.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m.CASCADE)
    good = m.ForeignKey(Good, on_delete=m.CASCADE)
    added_date = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.good.title
