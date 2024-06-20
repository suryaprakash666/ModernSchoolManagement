from django.db import models
from rest_framework import serializers

from .SubjectDataModel import Subjectdatamodel


class Classdatamodel(models.Model):
    Class_ID = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    subjects_assigned = models.ManyToManyField(Subjectdatamodel)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ClassDataModel'


class Classdataserializer(serializers.ModelSerializer):
    class Meta:
        model = Classdatamodel
        fields = '__all__'
