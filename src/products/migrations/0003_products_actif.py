# Generated by Django 4.0.1 on 2022-01-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_options_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
