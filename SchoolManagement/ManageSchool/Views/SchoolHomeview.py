import datetime
from django.shortcuts import render, redirect

from ..ModelsOfDatabase.StaffDataModel import Staffdatamodel
from ..ModelsOfDatabase.StudentDataModel import Studentdatamodel


def check_session(request):
    # print("Session Data After Login:", request.session.items())
    if 'school_id' not in request.session:
        # print("No school_id in session")
        return redirect('schoolloginlink')
    # print("school_id found in session:", request.session['school_id'])
    return None


def schoolhomeview(request):
    if check_session(request):
        return check_session(request)
    return render(request, 'SchoolHomeview.html')


def student_requests_tabview(request):
    if check_session(request):
        return check_session(request)
    # print("Accessing student_requests_tabview with session:", request.session.items())
    student_data = Studentdatamodel.objects.all()
    return render(request, 'StudentAdmissionRequestsTab.html', {'student_data': student_data})


def teacher_requests_tabview(request):
    if check_session(request):
        return check_session(request)
    # print("Accessing teacher_requests_tabview with session:", request.session.items())
    teachers = Staffdatamodel.objects.all()
    application_date = datetime.date.today()
    return render(request, 'Teacher-interview-request-tab.html', {'teachers': teachers, 'application_date': application_date})


def school_logout_view(request):
    if 'school_id' in request.session:
        del request.session['school_id']
        # print("Session Data Deleted")
    return render(request, 'Schoollogin.html')