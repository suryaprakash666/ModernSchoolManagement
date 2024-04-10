# views.py

from django.shortcuts import render, redirect
from ..Forms.SchoolForm import SchoolForm


def schoolloginview(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
           pass  # Assuming you have a URL named 'login'
    else:
        form = SchoolForm()
    return render(request, 'Studentlogin.html', {'form': form})
