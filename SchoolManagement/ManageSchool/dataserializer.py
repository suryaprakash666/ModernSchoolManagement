from rest_framework import serializers

from .models import Schooldatamodel, Staffdatamodel, Studentdatamodel


class Schooldataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schooldatamodel
        fields = '__all__'


class Staffdataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staffdatamodel
        fields = '__all__'


class Studentdataserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studentdatamodel
        fields = '__all__'


