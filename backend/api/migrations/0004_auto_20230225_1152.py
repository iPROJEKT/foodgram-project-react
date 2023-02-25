# Generated by Django 3.2 on 2023-02-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_weight_ingredients_measurement_unit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='tags',
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(max_length=200, to='api.Tag'),
        ),
    ]
