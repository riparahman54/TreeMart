# Generated by Django 5.1.3 on 2024-11-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tree_images/'),
        ),
    ]
