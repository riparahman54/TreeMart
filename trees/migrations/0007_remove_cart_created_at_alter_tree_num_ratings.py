# Generated by Django 5.1.3 on 2024-11-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0006_merge_20241129_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='tree',
            name='num_ratings',
            field=models.PositiveIntegerField(default=0),
        ),
    ]