# Generated by Django 2.0.1 on 2018-01-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_site', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]