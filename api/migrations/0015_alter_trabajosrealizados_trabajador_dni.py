# Generated by Django 5.0.1 on 2024-01-31 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_delete_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajosrealizados',
            name='trabajador_dni',
            field=models.ForeignKey(db_column='trabajador_dni', on_delete=django.db.models.deletion.CASCADE, to='api.trabajador'),
        ),
    ]
