from rest_framework import viewsets

from ..ModelsOfDatabase.ClassDataModel import Classdatamodel, Classdataserializer
from ..ModelsOfDatabase.SchoolDataModel import Schooldatamodel, Schooldataserializer
from ..ModelsOfDatabase.StaffDataModel import Staffdatamodel, Staffdataserializer
from ..ModelsOfDatabase.StudentDataModel import Studentdatamodel, Studentdataserializer
from ..ModelsOfDatabase.SubjectDataModel import Subjectdatamodel, Subjectdataserializer


class Schooldataviewset(viewsets.ModelViewSet):
    queryset = Schooldatamodel.objects.all()
    serializer_class = Schooldataserializer


class Staffdataviewset(viewsets.ModelViewSet):
    queryset = Staffdatamodel.objects.all()
    serializer_class = Staffdataserializer


class Studentdataviewset(viewsets.ModelViewSet):
    queryset = Studentdatamodel.objects.all()
    serializer_class = Studentdataserializer


class Classdataviewset(viewsets.ModelViewSet):
    queryset = Classdatamodel.objects.all()
    serializer_class = Classdataserializer


class SubjectViewset(viewsets.ModelViewSet):
    queryset = Subjectdatamodel.objects.all()
    serializer_class = Subjectdataserializer



