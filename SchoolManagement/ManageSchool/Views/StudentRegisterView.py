from django.http import JsonResponse
from django.shortcuts import render
from ..Forms.StudentForm import StudentForm
from ..ModelsOfDatabase.SchoolDataModel import Schooldatamodel
from ..ModelsOfDatabase.StudentDataModel import Studentdatamodel


def studentregisterview(request):
    if request.method == 'POST':
        school_name = request.POST.get('school')
        school = Schooldatamodel.objects.get(name=school_name)
        new_student = Studentdatamodel(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            passportphoto=request.FILES.get('passportphoto'),
            date_of_birth=request.POST.get('dob'),
            adharphoto=request.FILES.get('adharphoto'),
            fathername=request.POST.get('fathername'),
            mothername=request.POST.get('mothername'),
            parentmobile=request.POST.get('parentmobile'),
            street=request.POST.get('street'),
            city=request.POST.get('city'),
            locality=request.POST.get('locality'),
            state=request.POST.get('state'),
            school=school
        )
        new_student.save()
        form = StudentForm()
        return render(request, 'StudentLogin.html', {'form': form})
    return render(request, 'Studentregister.html', {'schools': Schooldatamodel.objects.all()})
