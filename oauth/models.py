from django.core.validators import FileExtensionValidator
from django.db import models as m


class AuthUser(m.Model):
    email = m.EmailField(max_length=150, unique=True)
    join_date = m.DateTimeField(auto_now_add=True)
    country = m.CharField(max_length=30, blank=True, null=True)
    city = m.CharField(max_length=30, blank=True, null=True)
    bio = m.TextField(max_length=2000, blank=True, null=True)
    display_name = m.CharField(max_length=30, blank=True, null=True)
    # avatar = m.ImageField(
    #     upload_to="photos/category/%m/%d/",
    #     verbose_name="Фото Категорий",
    #     default="empty.jfif",
    #     validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    # )

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email
