# Generated by Django 3.1.5 on 2021-02-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_auto_20210227_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='verified',
            field=models.IntegerField(choices=[(0, 'Not Verified'), (1, 'Verified')], default=0, help_text='please check this if you have verfieid the user'),
        ),
    ]
