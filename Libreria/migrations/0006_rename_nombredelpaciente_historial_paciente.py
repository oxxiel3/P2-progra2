# Generated by Django 4.2.7 on 2023-11-06 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libreria', '0005_historial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historial',
            old_name='nombreDelPaciente',
            new_name='paciente',
        ),
    ]
