# Generated by Django 2.2.7 on 2019-11-22 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0003_auto_20191121_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='find',
            name='count',
        ),
    ]
