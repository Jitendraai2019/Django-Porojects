# Generated by Django 2.2.5 on 2019-11-08 10:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191108_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 8, 10, 34, 13, 433580, tzinfo=utc)),
        ),
    ]