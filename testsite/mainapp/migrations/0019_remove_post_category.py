# Generated by Django 3.2.7 on 2023-03-08 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
