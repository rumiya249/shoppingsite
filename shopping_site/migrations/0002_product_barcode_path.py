# Generated by Django 2.0.1 on 2018-01-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Barcode_Path',
            field=models.ImageField(blank=True, null=True, upload_to='data_files/svg'),
        ),
    ]
