# Generated by Django 2.1.4 on 2019-01-04 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_course_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='Organization'),
        ),
    ]
