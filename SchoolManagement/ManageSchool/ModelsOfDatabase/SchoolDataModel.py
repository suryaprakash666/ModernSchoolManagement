from django.db import models
from rest_framework import serializers


class Schooldatamodel(models.Model):
    CATEGORY_CHOICES = [
        ('A++', 'A++'),
        ('A+', 'A+'),
        ('A', 'A'),
    ]

    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    passkey = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SchoolDataModel'
        verbose_name = 'SchoolDataModel'
        verbose_name_plural = 'SchoolDataModel'


class Schooldataserializer(serializers.ModelSerializer):
    class Meta:
        model = Schooldatamodel
        fields = '__all__'
