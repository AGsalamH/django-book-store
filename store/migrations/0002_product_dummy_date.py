# Generated by Django 3.2.4 on 2021-07-13 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dummy_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=''),
        ),
    ]
