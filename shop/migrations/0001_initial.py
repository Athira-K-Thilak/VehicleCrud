# Generated by Django 5.1.4 on 2024-12-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=200)),
                ('fuel_type', models.CharField(max_length=200)),
                ('specs', models.TextField(max_length=300)),
            ],
        ),
    ]
