# Generated by Django 3.2.7 on 2023-03-08 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20230308_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Camera_height',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Distance_to_door',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Door_with',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Zoom_perc',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title2',
        ),
    ]
