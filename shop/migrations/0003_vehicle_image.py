# Generated by Django 5.1.4 on 2025-01-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_vehicle_specs'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(null=True, upload_to='vehicleimages'),
        ),
    ]
