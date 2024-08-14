import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..ModelsOfDatabase.StaffDataModel import Staffdatamodel
from ..ModelsOfDatabase.StudentDataModel import Studentdatamodel


@login_required(login_url='schoolloginlink')
@csrf_exempt
def schoolhomeview(request):
    return render(request, 'SchoolHomeview.html')


@csrf_exempt
def student_requests_tabview(request):
    student_data = Studentdatamodel.objects.all()
    return render(request, 'StudentAdmissionRequestsTab.html', {'student_data': student_data})


def teacher_requests_tabview(request):
    teachers = Staffdatamodel.objects.all()
    application_date = datetime.date.today()
    return render(request, 'Teacher-interview-request-tab.html', {'teachers': teachers, 'application_date': application_date})


def clean_interview_request(teacher_id):
    teacher = Staffdatamodel.objects.get(id=teacher_id)
    teacher.delete()
    return redirect('teacher_requests_tabview')



