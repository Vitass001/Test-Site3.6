# Generated by Django 3.2.7 on 2023-03-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_post_title1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
