from django.db import models
from rest_framework import serializers

from .SubjectDataModel import Subjectdatamodel


class Staffdatamodel(models.Model):
    staff_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=120)
    name = models.CharField(max_length=100)
    steert = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
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
