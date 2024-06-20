# views.py

from django.shortcuts import render, redirect
from ..Forms.StaffForm import StaffForm


def staffloginview(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            pass
            # Redirect to a success page or login page
    else:
        form = StaffForm()
    return render(request, 'Stafflogin.html', {'form': form})
