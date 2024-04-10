# views.py

from django.shortcuts import render, redirect
from ..Forms.StudentForm import StudentForm


def studentloginview(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # Assuming you have a URL named 'login'
    else:
        form = StudentForm()
    return render(request, 'Studentlogin.html', {'form': form})
