# Generated by Django 3.1.5 on 2021-02-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartcity_app', '0004_auto_20210219_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
    ]
