# Generated by Django 3.0.4 on 2020-04-05 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200402_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='titulo',
        ),
    ]
