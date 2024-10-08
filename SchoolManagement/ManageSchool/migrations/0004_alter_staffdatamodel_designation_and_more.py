# Generated by Django 5.0.6 on 2024-08-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageSchool', '0003_staffdatamodel_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdatamodel',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staffdatamodel',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='staffdatamodel',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
