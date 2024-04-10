from django.shortcuts import render

def homepageview(request):
    if request.method == 'POST':
        button_clicked = request.POST.get('buttonclicked',None)
        if button_clicked == 'adminregister':
            return render(request,'SchoolSignMethod.html')
        elif button_clicked == 'staffregister':
            return render(request,'StaffSignMethod.html')
        elif button_clicked == 'studentregister':
            return render(request,'StudentSignMethod.html')
    elif request.method == 'GET':    
        return render(request,'HomeView.html')
