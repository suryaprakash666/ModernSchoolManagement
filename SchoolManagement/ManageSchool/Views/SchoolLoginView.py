import hashlib
from django.shortcuts import render, redirect
from ..Forms.SchoolForm import SchoolForm
from ..ModelsOfDatabase.SchoolDataModel import Schooldatamodel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def schoolloginview(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if not form.is_valid():
            print(form.errors)  # Print form errors if the form is not valid
        else:
            email = form.cleaned_data.get('email')
            passkey = form.cleaned_data.get('passkey')
            hashed_passkey = hashlib.md5(passkey.encode()).hexdigest()
            # Check if a Schooldatamodel instance exists with the given email and passkey
            user_exists = Schooldatamodel.objects.filter(email=email, passkey=hashed_passkey).exists()
            if user_exists:
                user = Schooldatamodel.objects.get(email=email, passkey=hashed_passkey)
                request.session['school_id'] = user.id
                # Pass the school name to the rendered page
                return render(request, 'SchoolHomeview.html', {'form': form, 'school': user})
            else:
                return render(request, 'Schoollogin.html', {'form': form, 'error': 'Invalid email or passkey'})
    else:
        form = SchoolForm()
    return render(request, 'Schoollogin.html', {'form': form})
