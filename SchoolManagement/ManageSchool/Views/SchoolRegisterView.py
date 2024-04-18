from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ..Forms.SchoolForm import SchoolForm
from ..models import Schooldatamodel


@csrf_exempt
def schoolregisterview(request):
    if request.method == 'POST':
        schoolname = request.POST.get('schoolname')
        schoolemail = request.POST.get('email')
        schoolestablished = request.POST.get('schoolestab')
        state = request.POST.get('state')
        district = request.POST.get('district')
        locality = request.POST.get('locality')
        pincode = request.POST.get('pincode')

        school = Schooldatamodel(School_Name=schoolname,
                                 School_Email=schoolemail,
                                 School_Established=schoolestablished,
                                 School_State=state,
                                 School_District=district,
                                 School_Locality=locality,
                                 School_Pincode=pincode)
        school.save()
        form = SchoolForm()
        return render(request, 'Schoollogin.html', {'form': form})
    else:
        return render(request, 'SchoolRegister.html')
