# Generated by Django 3.1.5 on 2021-02-28 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_userprofile_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]
