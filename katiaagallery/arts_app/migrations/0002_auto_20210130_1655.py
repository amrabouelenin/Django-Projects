# Generated by Django 3.1.5 on 2021-01-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='art_img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]