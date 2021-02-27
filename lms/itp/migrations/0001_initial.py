# Generated by Django 3.1.5 on 2021-02-27 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=256, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_name', models.CharField(max_length=256, verbose_name='Section Name')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sec_dep', to='itp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=256, verbose_name='Unit Name')),
                ('sec_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit_sec', to='itp.section')),
            ],
        ),
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=256, verbose_name='Standard ITP Role')),
                ('unit_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobrole_unit', to='itp.unit')),
            ],
        ),
    ]