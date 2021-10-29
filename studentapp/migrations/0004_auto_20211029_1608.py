# Generated by Django 3.2.8 on 2021-10-29 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20211029_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattend',
            name='atten_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='studentattend',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='studentattend',
            name='in_time',
            field=models.TimeField(default='09:00'),
        ),
        migrations.AlterField(
            model_name='studentattend',
            name='out_time',
            field=models.TimeField(default='09:00'),
        ),
    ]
