# Generated by Django 3.1.5 on 2021-02-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_name', models.CharField(max_length=256, unique=True, verbose_name='Entity Name')),
                ('entity_code', models.CharField(max_length=256, unique=True, verbose_name='Entity Code')),
            ],
        ),
    ]
