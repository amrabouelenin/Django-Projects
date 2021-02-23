# Generated by Django 3.1.5 on 2021-02-20 14:18

from django.db import migrations, models
import geolocation_fields.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('smartcity_app', '0007_auto_20210220_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_name', models.CharField(help_text='Please write the station name i.e Lodz Fabrycna', max_length=256)),
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', geolocation_fields.models.fields.PointField(help_text='Please drag the mouse to the location of the station', verbose_name='location')),
            ],
        ),
        migrations.AddConstraint(
            model_name='station',
            constraint=models.UniqueConstraint(fields=('station_name',), name='unique_station_name'),
        ),
    ]
