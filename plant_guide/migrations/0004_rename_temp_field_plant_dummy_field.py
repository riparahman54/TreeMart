# Generated by Django 5.1.3 on 2024-11-30 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_guide', '0003_plant_temp_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='temp_field',
            new_name='dummy_field',
        ),
    ]
