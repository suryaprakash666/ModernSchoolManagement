from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..ModelsOfDatabase.StudentDataModel import Studentdatamodel


@login_required(login_url='schoolloginlink')
@csrf_exempt
def schoolhomeview(request):
    return render(request, 'SchoolHomeview.html')


@csrf_exempt
def student_requests_tabview(request):
    student_data = Studentdatamodel.objects.all()
    return render(request, 'StudentAdmissionRequestsTab.html', {'student_data': student_data})
