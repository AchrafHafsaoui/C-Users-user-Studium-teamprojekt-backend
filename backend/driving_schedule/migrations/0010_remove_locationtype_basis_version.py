# Generated by Django 5.1.4 on 2024-12-26 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driving_schedule', '0009_remove_drivingschedule_arr_location_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationtype',
            name='basis_version',
        ),
    ]