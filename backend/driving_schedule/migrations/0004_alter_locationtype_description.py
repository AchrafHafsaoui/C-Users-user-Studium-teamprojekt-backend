# Generated by Django 5.1.3 on 2024-12-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving_schedule', '0003_locationtype_remove_drivingschedule_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationtype',
            name='description',
            field=models.CharField(max_length=60),
        ),
    ]