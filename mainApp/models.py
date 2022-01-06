from django.db import models as m
from django.urls import reverse

from slugify import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = m.CharField(max_length=255, verbose_name="Имя категории", unique=True)
    parent = TreeForeignKey("self", on_delete=m.CASCADE, null=True, blank=True, related_name="children")
    photo = m.ImageField(upload_to="photos/category/%m/%d/", verbose_name="Фото Категорий",
                         default="empty.jfif")

    is_published = m.BooleanField(default=True, verbose_name="Опубликовано ?")

    created_dt = m.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_dt = m.DateTimeField(auto_now=True, verbose_name="Дата оновления")

    slug = m.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    class MPTTMeta:
        order_insertion_by = ["title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}")
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Good(m.Model):
    title = m.CharField(max_length=250, verbose_name="Заголовок товара")
    subtitle = m.CharField(max_length=250, verbose_name="Под заголовок товара")
    description = m.TextField(verbose_name="Описание товара", blank=True, null=True)
    price = m.PositiveIntegerField(verbose_name="Цена")
    photo = m.ImageField(upload_to="photos/goods/%m/%d/", verbose_name="Фото товара", default="empty.jfif")

    is_published = m.BooleanField(default=True, verbose_name="Опулбиковано ?")

    created_dt = m.DateTimeField(auto_now_add=True)
    updated_dt = m.DateTimeField(auto_now=True)

    category = TreeForeignKey(Category, on_delete=m.CASCADE, blank=False,
                              null=False, verbose_name=u'Раздел')

    slug = m.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}")
        super(Good, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('good_detail', kwargs={'slug': self.slug})



