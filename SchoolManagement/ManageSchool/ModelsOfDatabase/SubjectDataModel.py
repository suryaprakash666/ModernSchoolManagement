from django.db import models
from rest_framework import serializers


class Subjectdatamodel(models.Model):
    Subject_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SubjectDataModel'
        verbose_name = 'SubjectDataModel'
        verbose_name_plural = 'SubjectDataModel'
        ordering = ['Subject_ID']
        unique_together = (('name', 'description'),)


class Subjectdataserializer(serializers.ModelSerializer):
    class Meta:
        model = Subjectdatamodel
        fields = '__all__'
