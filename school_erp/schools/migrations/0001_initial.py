# Generated by Django 5.1.2 on 2025-02-05 00:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('principal', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('contact_phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
                'db_table': 'school',
            },
        ),
    ]
