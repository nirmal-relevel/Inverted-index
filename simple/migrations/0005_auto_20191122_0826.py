# Generated by Django 2.2.7 on 2019-11-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0004_remove_find_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='words',
            field=models.IntegerField(),
        ),
    ]
