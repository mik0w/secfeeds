# Generated by Django 3.2.10 on 2022-01-06 19:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddata',
            name='feed_url',
            field=models.URLField(max_length=350, unique=True),
        ),
        migrations.CreateModel(
            name='FeedMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='n/a', max_length=500)),
                ('title_detail', models.TextField(default='n/a')),
                ('published', models.DateTimeField(default=datetime.date(2022, 1, 6))),
                ('link', models.URLField(max_length=350, unique=True)),
                ('feed_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.feeddata')),
            ],
        ),
    ]
