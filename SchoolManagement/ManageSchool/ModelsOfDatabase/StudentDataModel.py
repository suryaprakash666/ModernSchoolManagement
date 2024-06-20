from django.db import models
from rest_framework import serializers

from .ClassDataModel import Classdatamodel
from .SchoolDataModel import Schooldatamodel


class Studentdatamodel(models.Model):
    student_id = models.AutoField(primary_key=True, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    passportphoto = models.ImageField(upload_to='UserUploadedFiles/')
    adharphoto = models.ImageField(upload_to='UserUploadedFiles/', null=True)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    parentmobile = models.CharField(max_length=10)
    street = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, unique=True, null=True, blank=True)
    date_of_birth = models.DateField()
    class_name = models.ForeignKey(Classdatamodel, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(Schooldatamodel, on_delete=models.CASCADE, null=True)
    id_valid_till = models.DateField(null=True)
    registered_student = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Meta:
    db_table = 'studentdatamodel'


class Studentdataserializer(serializers.ModelSerializer):
    class Meta:
        model = Studentdatamodel
        fields = '__all__'
