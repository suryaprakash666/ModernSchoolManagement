# Generated by Django 5.1.2 on 2025-02-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_studentregistration_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
