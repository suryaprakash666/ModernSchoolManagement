from django.shortcuts import render,HttpResponse

from ..ModelsOfDatabase.SchoolDataModel import Schooldatamodel
from ..ModelsOfDatabase.StaffDataModel import Staffdatamodel


def staffregisterview(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        passportphoto = request.FILES.get('passportphoto')
        adharphoto = request.FILES.get('adharphoto')
        qualification = request.POST.get('qualification')
        qualification_certificate = request.FILES.get('qualification-certificate')
        school = request.POST.get('school')
        state = request.POST.get('state')
        city = request.POST.get('city')
        locality = request.POST.get('locality')
        pincode = request.POST.get('pincode')
        schoolname = Schooldatamodel.objects.get(name=school)
        # Now you can use these variables to create a new Staffdatamodel instance or for other purposes
        # For example:
        staff = Staffdatamodel(name=firstname+lastname, email=email, passportphoto=passportphoto, adharphoto=adharphoto,
                               qualification_certificate=qualification_certificate, qualification=qualification,
                               state=state, city=city, locality=locality, pincode=pincode, school=schoolname)
        staff.save()
        return HttpResponse('Staff registered successfully')
    schools = Schooldatamodel.objects.all()
    return render(request, 'Staffregister.html', {'schools': schools})
