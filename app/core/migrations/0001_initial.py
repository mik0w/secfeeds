# Generated by Django 3.2.10 on 2021-12-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedData',
            fields=[
                ('feed_url', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('is_verified', models.BooleanField()),
            ],
        ),
    ]