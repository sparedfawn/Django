# Generated by Django 3.2 on 2021-04-07 21:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210407_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='content',
            field=models.FileField(default='Default value', upload_to=''),
        ),
        migrations.AlterField(
            model_name='publiclink',
            name='generationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 21, 17, 9, 865524, tzinfo=utc)),
        ),
    ]
