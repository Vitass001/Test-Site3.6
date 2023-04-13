# Generated by Django 4.1.7 on 2023-03-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_remove_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Test_instaler',
            new_name='Angle_to_face_Degrees',
        ),
        migrations.AddField(
            model_name='post',
            name='Distance_from_door',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Door_entrance_width',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Facebox_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Height',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Install_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Installer_Company',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Installer_email',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Kasa_login',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Phone_Model',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Phone_Serial_No',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Pixels_per_face',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Router_Serial_No',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Video_on_teams',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
