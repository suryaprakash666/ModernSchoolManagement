from rest_framework import viewsets
from ..dataserializer import Schooldataserializer, Staffdataserializer, Studentdataserializer
from ..models import Schooldatamodel, Staffdatamodel, Studentdatamodel


class Dataviewset(viewsets.ModelViewSet):
    queryset = Schooldatamodel.objects.all()
    serializer_class = Schooldataserializer


class Staffdataviewset(viewsets.ModelViewSet):
    queryset = Staffdatamodel.objects.all()
    serializer_class = Staffdataserializer


class Studentdataviewset(viewsets.ModelViewSet):
    queryset = Studentdatamodel.objects.all()
    serializer_class = Studentdataserializer
    
