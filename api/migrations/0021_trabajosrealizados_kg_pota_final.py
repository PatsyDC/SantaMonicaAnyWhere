# Generated by Django 5.0.1 on 2024-02-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_rename_creado_por_user_trabajosrealizados_creado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajosrealizados',
            name='kg_Pota_final',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
