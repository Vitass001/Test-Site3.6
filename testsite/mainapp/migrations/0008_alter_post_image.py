# Generated by Django 3.2.7 on 2023-03-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='mainapp/static/mainapp/images/', width_field='width_field'),
        ),
    ]
