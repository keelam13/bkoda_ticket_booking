# Generated by Django 5.1.7 on 2025-03-19 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_reservation_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='total_number_of_seats',
            new_name='total_seats',
        ),
    ]
