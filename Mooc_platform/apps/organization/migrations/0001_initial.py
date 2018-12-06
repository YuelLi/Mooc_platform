# Generated by Django 2.1.2 on 2018-12-03 07:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='City Name')),
                ('desc', models.CharField(max_length=200, verbose_name='City Description')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Organization Name')),
                ('desc', models.CharField(max_length=200, verbose_name='Organization')),
                ('click_num', models.IntegerField(default=0, verbose_name='click numbers')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='favorites number')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='cover image')),
                ('address', models.CharField(max_length=150, verbose_name='Organization Address')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='Located City')),
            ],
            options={
                'verbose_name': 'Course Organization',
                'verbose_name_plural': 'Course Organizations',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Instructor Name')),
                ('work_years', models.IntegerField(default=0, verbose_name='work years')),
                ('company', models.CharField(max_length=50, verbose_name='company works for')),
                ('position', models.CharField(max_length=50, verbose_name='position')),
                ('feature', models.CharField(max_length=50, verbose_name='teaching feature')),
                ('click_num', models.IntegerField(default=0, verbose_name='click numbers')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='favorites number')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='Organization at')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
            },
        ),
    ]
