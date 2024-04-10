from django.shortcuts import render
from ManageSchool.models import Studentdatamodel, Schooldatamodel
from django.http import HttpResponse

def studentregisterview(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        passportphoto = request.FILES.get('passportphoto')
        adharphoto = request.FILES.get('adharphoto')
        contact = request.POST.get('parentmobile')
        state = request.POST.get('state')
        district = request.POST.get('district')
        locality = request.POST.get('locality')
        pincode = request.POST.get('pincode')
        school_name = request.POST.get('school')
        school = Schooldatamodel.objects.get(School_Name=school_name)

        student = Studentdatamodel(Student_Firstname=firstname, Student_Lastname=lastname, Student_DateofBirth=dob,
                                   Student_Passportphoto=passportphoto, Student_Adharphoto=adharphoto,
                                   Student_Contact=contact, Student_State=state, Student_District=district,
                                   Student_Locality=locality, Student_Pincode=pincode, Student_School=school)
        student.save()
        return HttpResponse('registered')
    elif request.method == 'GET':
        schoollist = Schooldatamodel.objects.values_list('School_Name', flat=True)
        return render(request, 'StudentAddmission.html',{'schoollist':schoollist})