# Generated by Django 4.1.7 on 2023-03-12 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_favoriterecipe_recipe_alter_recipe_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='pub_date',
        ),
    ]