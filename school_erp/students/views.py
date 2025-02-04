from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from schools.models import School
from students.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from Baseuser.models import BaseUser
from .models import StudentRegistration

# Homepage view
@login_required
def homepageview(request):
    return render(request, 'StudentHome.html')



# Registration view
def registrationview(request):
    if request.method == 'POST':
        # Extracting form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')  # Assuming date_of_birth is provided as 'YYYY-MM-DD'
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')
        school_id = request.POST.get('school')
        aadhar_card = request.FILES.get('adharcard')  # Aadhar card file
        passport_photo = request.FILES.get('passportphoto')  # Passport photo file
        tc = request.FILES.get('tc')  # Transfer certificate file (optional)

        # Validation checks
        if not all([first_name, last_name, email, phone, date_of_birth, address, city, state, country, pincode, school_id, aadhar_card, passport_photo]):
            messages.error(request, "All fields are required!")
            return render(request, 'StudentRegistration.html')

        if '@' not in email:
            messages.error(request, "Please provide a valid email address.")
            return render(request, 'StudentRegistration.html')

        if not phone.isdigit() or len(phone) < 10:
            messages.error(request, "Please provide a valid phone number.")
            return render(request, 'StudentRegistration.html')

        # Save files
        fs = FileSystemStorage()
        try:
            aadhar_card_url = fs.save(aadhar_card.name, aadhar_card)
            passport_photo_url = fs.save(passport_photo.name, passport_photo)
            tc_url = fs.save(tc.name, tc) if tc else None

            # Get the selected school
            school = School.objects.get(id=school_id)

            # Create and save StudentRegistration object
            student_registration = StudentRegistration(
                school=school,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                email=email,
                phone=phone,
                address=address,
                city=city,
                state=state,
                country=country,
                pincode=pincode,
                adharcard=aadhar_card_url,
                passportphoto=passport_photo_url,
                tc=tc_url,
                is_verified=False
            )
            student_registration.save()

            messages.success(request, "Registration request submitted successfully!")
            print("Registration request submitted successfully!")
            return redirect('studentloginurl')

        except Exception as e:
            messages.error(request, "Error processing your request. Please try again.")
            print(f"Error processing registration request: {e}")
            return render(request, 'StudentRegistration.html')

    schools = School.objects.all()
    return render(request, 'StudentRegistration.html', {'schools': schools})




# Login view
from django.contrib.auth.hashers import check_password
@csrf_exempt
def loginview(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print("Attempting login with:")
        print(f"Email: {email}")
        print(f"Password: {password}")

        # Try to fetch the user directly first
        print("Checking if user exists:")
        try:
            user_obj = Student.objects.get(email=email)
            print(f"User found: {user_obj}")

            # Check if the password matches using the check_password method
            if user_obj.check_password(password):
                print("Password matches!")
                print(request.session.items())
                # If password matches, manually log in the user
                login(request, user_obj)
                return redirect("studenthomeurl")  # Redirect to the home page after successful login
            else:
                print("Password doesn't match.")
                messages.error(request, "Invalid email or password.")
                return redirect("studentloginurl")
                
        except Student.DoesNotExist:
            print("No user found with this email")
            messages.error(request, "No user found with this email.")
            return redirect("studentloginurl")

    return render(request, "StudentLogin.html")

# Logout view
def logoutview(request):
    logout(request)
    return redirect("studentloginurl")

def clearsession(request):
    request.session.clear()
    request.Session.flush()
    return HttpResponse("Session cleared")