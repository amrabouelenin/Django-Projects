# Generated by Django 3.1.5 on 2021-02-13 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arts_app', '0007_auto_20210213_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='arts_app.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='discription',
            field=models.TextField(blank=True, help_text='Write an interesting text about you here'),
        ),
    ]