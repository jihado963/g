# Generated by Django 2.2.2 on 2019-06-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_auto_20190617_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personm',
            name='email',
            field=models.EmailField(max_length=64),
        ),
        migrations.AlterField(
            model_name='personm',
            name='f_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='personm',
            name='l_name',
            field=models.CharField(max_length=32),
        ),
    ]