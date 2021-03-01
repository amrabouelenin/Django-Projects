# Generated by Django 3.1.5 on 2021-02-28 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('itp', '0001_initial'),
        ('userprofile', '0015_auto_20210228_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='ITP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026)], default=2021, verbose_name='ITP year')),
                ('itp_state', django_fsm.FSMField(choices=[('draft', 'draft'), ('submitted', 'Submitted')], default='draft', max_length=50, verbose_name='ITP Submission Status')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='itp.department')),
                ('job_role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='itp.jobrole')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]