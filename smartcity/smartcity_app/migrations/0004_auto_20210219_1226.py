# Generated by Django 3.1.5 on 2021-02-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartcity_app', '0003_auto_20210219_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beacon',
            name='id',
        ),
        migrations.AddField(
            model_name='beacon',
            name='beacon_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
