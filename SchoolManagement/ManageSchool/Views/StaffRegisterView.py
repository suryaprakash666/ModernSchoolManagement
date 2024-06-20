from django.shortcuts import render
from ..ModelsOfDatabase.SchoolDataModel import Schooldatamodel


def staffregisterview(request):
    if request.method == 'POST':
        pass
    schools = Schooldatamodel.objects.all()
    return render(request, 'Staffregister.html', {'schools': schools})
