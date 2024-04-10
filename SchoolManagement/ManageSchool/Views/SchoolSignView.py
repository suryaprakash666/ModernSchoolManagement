from django.shortcuts import render


def schoolsignview(request):
    return render(request, 'SchoolSignMethod.html')
