# Generated by Django 3.1.5 on 2021-02-27 07:47

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20210227_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nationality',
            field=django_countries.fields.CountryField(default=1, max_length=2),
        ),
    ]