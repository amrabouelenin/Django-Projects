# Generated by Django 3.1.5 on 2021-02-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itp', '0001_initial'),
        ('userprofile', '0002_auto_20210226_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='test_field',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Job_role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_jobrole', to='itp.jobrole'),
        ),
    ]