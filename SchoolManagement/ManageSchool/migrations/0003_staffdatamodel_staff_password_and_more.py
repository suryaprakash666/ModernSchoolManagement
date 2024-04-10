# Generated by Django 4.2.11 on 2024-04-10 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageSchool', '0002_alter_studentdatamodel_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdatamodel',
            name='Staff_Password',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='studentdatamodel',
            name='Student_Password',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='staffdatamodel',
            name='Staff_Adharpic',
            field=models.ImageField(default='', upload_to='UserUploadedFiles/'),
        ),
        migrations.AlterField(
            model_name='staffdatamodel',
            name='Staff_Profilepic',
            field=models.ImageField(default='', upload_to='UserUploadedFiles/'),
        ),
        migrations.AlterField(
            model_name='studentdatamodel',
            name='Student_Adharphoto',
            field=models.ImageField(default='', upload_to='UserUploadedFiles/'),
        ),
        migrations.AlterField(
            model_name='studentdatamodel',
            name='Student_Passportphoto',
            field=models.ImageField(default='', upload_to='UserUploadedFiles/'),
        ),
    ]
