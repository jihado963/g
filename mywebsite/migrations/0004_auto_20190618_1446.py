# Generated by Django 2.2.2 on 2019-06-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0003_auto_20190617_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personm',
            name='phone_num',
            field=models.CharField(max_length=13),
        ),
    ]
