# Generated by Django 3.2.7 on 2023-03-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20230308_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='camera_height',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='distance_to_door',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='door_with',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='zoom_perc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
