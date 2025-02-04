# Generated by Django 5.1.2 on 2025-02-03 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='principal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_principal', to='staffs.staff'),
        ),
    ]
