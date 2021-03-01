# Generated by Django 3.1.5 on 2021-02-28 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20210228_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=255, unique=True, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255, unique=True, verbose_name='Vendor Name')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_method', models.CharField(choices=[('EC', 'E-Learning Classes'), ('FFC', 'Face To Face Classes'), ('BC', 'Blinded Classes')], default='EC', max_length=256, verbose_name='Course delivery method')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.course')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.location')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.vendor')),
            ],
        ),
    ]
