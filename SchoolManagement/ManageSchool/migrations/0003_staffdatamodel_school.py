# Generated by Django 5.0.6 on 2024-08-10 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageSchool', '0002_remove_staffdatamodel_steert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdatamodel',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ManageSchool.schooldatamodel'),
        ),
    ]
