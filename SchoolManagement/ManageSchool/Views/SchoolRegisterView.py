import hashlib
from django.shortcuts import render, HttpResponse
from ..Forms.SchoolForm import SchoolForm
from ..ModelsOfDatabase.SchoolDataModel import Schooldatamodel


def schoolregisterview(request):
    if request.method == 'POST':
        school_name = request.POST.get('schoolname')
        school_email = request.POST.get('email')
        passkey = request.POST.get('passkey')
        confirm_passkey = request.POST.get('reEnter-passkey')
        street = request.POST.get('street')
        city = request.POST.get('city')
        locality = request.POST.get('locality')
        state = request.POST.get('state')

        if passkey == confirm_passkey:
            hashed_passkey = hashlib.md5(passkey.encode()).hexdigest()
            school = Schooldatamodel(name=school_name, email=school_email, passkey=hashed_passkey, street=street,
                                     city=city, locality=locality, state=state)
            school.save()
            form = SchoolForm()
            return render(request, 'Schoollogin.html', {'form': form})
        else:
            return HttpResponse("Passkey and Confirm Passkey do not match")

    else:
        return render(request, 'SchoolRegister.html')
