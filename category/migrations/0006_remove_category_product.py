# Generated by Django 5.0.1 on 2024-02-04 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
    ]