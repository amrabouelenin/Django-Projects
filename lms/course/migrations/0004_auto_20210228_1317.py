# Generated by Django 3.1.5 on 2021-02-28 13:17

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_prerequisites_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_certification',
            field=djrichtextfield.models.RichTextField(default='Course Certification', help_text='Write the course certification', verbose_name='Certification'),
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[(2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026)], default=2021),
        ),
    ]