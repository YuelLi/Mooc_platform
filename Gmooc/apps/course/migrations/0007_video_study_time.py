# Generated by Django 2.1.4 on 2019-01-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20190106_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='study_time',
            field=models.IntegerField(default=0, verbose_name='Study time (min)'),
        ),
    ]
