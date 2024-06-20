from django.contrib.auth import authenticate, login
from django.shortcuts import render
from ..Forms.StudentForm import StudentForm
from ..ModelsOfDatabase.StudentDataModel import Studentdatamodel


def studentloginview(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            parentmobile = form.cleaned_data['parentmobile']
            password = form.cleaned_data['password']
            try:
                student = Studentdatamodel.objects.get(parentmobile=parentmobile, password=password)
                if student.registered_student:
                    user = authenticate(request, username=parentmobile, password=password)
                    if user is not None:
                        login(request, user)
                        return render(request, 'Studentlogin.html', {'username': student.firstname + " " + student.lastname})
                    else:
                        return render(request, 'Studentview.html', {'form': form, 'error_message': 'Invalid username or password.', 'student': student})
                else:
                    return render(request, 'Studentview.html', {'form': form, 'error_message': 'Student is not registered.', 'student': student})
            except Studentdatamodel.DoesNotExist:
                return render(request, 'Studentview.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = StudentForm()
    return render(request, 'Studentlogin.html', {'form': form})
