# Generated by Django 2.0.6 on 2018-06-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0013_auto_20180629_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]