# Generated by Django 4.1.7 on 2023-03-08 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriterecipe',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='pub_date',
        ),
    ]