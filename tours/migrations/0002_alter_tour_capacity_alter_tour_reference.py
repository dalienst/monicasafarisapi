# Generated by Django 5.1.4 on 2025-01-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='capacity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='reference',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
