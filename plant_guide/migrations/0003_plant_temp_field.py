# Generated by Django 5.1.3 on 2024-11-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_guide', '0002_remove_plant_id_remove_plant_name_plant_tree_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='temp_field',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
