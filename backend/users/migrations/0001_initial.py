# Generated by Django 5.1.4 on 2024-12-10 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('active_user', 'Active User'), ('passive_user', 'Passive User')], default='passive_user', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]