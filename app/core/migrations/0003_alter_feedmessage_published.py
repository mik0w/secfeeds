# Generated by Django 3.2.10 on 2022-02-01 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220106_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedmessage',
            name='published',
            field=models.DateTimeField(default=datetime.date(2022, 2, 1)),
        ),
    ]