# Generated by Django 3.1.1 on 2022-12-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display_on_main_page',
            field=models.BooleanField(default=False),
        ),
    ]
