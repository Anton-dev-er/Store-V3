# Generated by Django 4.0 on 2022-01-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='empty.jfif', upload_to='photos/category/%m/%d/', verbose_name='Фото Категорий'),
        ),
    ]
