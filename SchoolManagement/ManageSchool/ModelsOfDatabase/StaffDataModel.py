from django.db import models
from rest_framework import serializers

from .SchoolDataModel import Schooldatamodel
from .SubjectDataModel import Subjectdatamodel


class Staffdatamodel(models.Model):
    staff_id = models.AutoField(primary_key=True)
    # Personal Details
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    passportphoto = models.ImageField(upload_to='UserUploadedFiles/', null=True)
    adharphoto = models.ImageField(upload_to='UserUploadedFiles/', null=True)
    qualification = models.CharField(max_length=100, null=True)
    qualification_certificate = models.ImageField(upload_to='UserUploadedFiles/', null=True)

    # Address Details
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=6, null=True)

    # other fields
    school = models.ForeignKey(Schooldatamodel, on_delete=models.CASCADE, null=True)
    designation = models.CharField(max_length=100, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    hire_date = models.DateField(null=True)
    subject_to_tought = models.ManyToManyField(Subjectdatamodel, blank=True)
    id_valid_till = models.DateField(null=True)
    registered_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'StaffDataModel'


class Staffdataserializer(serializers.ModelSerializer):
    subject_to_tought = serializers.PrimaryKeyRelatedField(
        queryset=Subjectdatamodel.objects.all(),  # Queryset for subjects
        many=True,  # Allow multiple subjects
        required=False  # Allow the field to be optional
    )

    class Meta:
        model = Staffdatamodel
        fields = '__all__'
