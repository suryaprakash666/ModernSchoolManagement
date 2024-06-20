from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def studenthomeview(request):
    return render(request, 'StudentHomeview.html')