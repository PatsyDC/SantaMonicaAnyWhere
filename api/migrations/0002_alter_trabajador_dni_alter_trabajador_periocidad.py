# Generated by Django 5.0.1 on 2024-01-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='dni',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='periocidad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
