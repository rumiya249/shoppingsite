# Generated by Django 2.0.1 on 2018-01-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_site', '0005_auto_20180126_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('path', models.FileField(upload_to='home/rumiya/workspace/')),
            ],
        ),
    ]
