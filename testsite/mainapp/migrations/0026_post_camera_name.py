# Generated by Django 4.1.7 on 2023-03-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_rename_test_instaler_post_angle_to_face_degrees_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Camera_Name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
