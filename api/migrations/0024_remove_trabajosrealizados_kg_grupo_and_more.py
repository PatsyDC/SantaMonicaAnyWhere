# Generated by Django 5.0.1 on 2024-02-05 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_trabajosrealizados_kg_grupo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajosrealizados',
            name='kg_grupo',
        ),
        migrations.RemoveField(
            model_name='trabajosrealizados',
            name='promedio_kg',
        ),
    ]
