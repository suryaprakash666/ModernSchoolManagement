from django.shortcuts import render
from django.http import HttpResponse
from ..models import Schooldatamodel, Staffdatamodel
from ..Forms.StaffForm import StaffForm

def staffregisterview(request):
    # Handle POST request when submitting staff registration form
    if request.method == 'POST':
        # Retrieve data from the POST request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        passportphoto = request.POST.get('passportphoto')
        adharphoto = request.POST.get('adharphoto')
        qualification = request.POST.get('qualification')
        q_certificate = request.POST.get('qualification-certificate')
        state = request.POST.get('state')
        district = request.POST.get('district')
        locality = request.POST.get('locality')
        pincode = request.POST.get('pincode')
        school_name = request.POST.get('school')
        
        # Retrieve the School object based on the school name
        school = Schooldatamodel.objects.get(School_Name=school_name)        

        # Create a new Staffdatamodel instance and save it to the database
        Staff = Staffdatamodel(Staff_Firstname=firstname, Staff_Lastname=lastname, Staff_Profilepic=passportphoto,
                               Staff_Adharpic=adharphoto, Staff_Qualification=qualification, Staff_State=state,
                               Staff_District=district, Staff_Locality=locality, Staff_Pincode=pincode, School_Name=school)
        Staff.save()
        form = StaffForm()
        return render(request, 'Stafflogin.html', {'form': form})
    # Handle GET request to render the staff registration form
    elif request.method == 'GET':
        # Retrieve a list of school names to populate the school selection dropdown
        schoollist = Schooldatamodel.objects.values_list('School_Name', flat=True)
        
        # Render the staff registration form template with the school list
        return render(request, 'Staffregister.html', {'schoollist': schoollist})