# Generated by Django 2.0.6 on 2018-06-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0003_doctorlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorlist',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='doctor_profile/'),
        ),
    ]
