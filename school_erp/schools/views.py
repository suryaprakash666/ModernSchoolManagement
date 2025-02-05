from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from schools.models import School
from students.models import Student, StudentRegister
from Baseuser.models import BaseUser


# View for schoolhomepage
@login_required
def schoolhomeview(request):
    username = request.session.get('username', 'guest')
    return render(request, 'SchoolHome.html', {'username': username})




# View for schoolregisterpage
def schoolregisterview(request):
    if request.method == 'POST':
        # Extract form data for School
        school_name = request.POST.get('school-name')
        school_address = request.POST.get('school-address')
        school_city = request.POST.get('school-city')
        school_state = request.POST.get('school-state')
        school_country = request.POST.get('school-country')
        school_pincode = request.POST.get('school-pincode')
        school_email = request.POST.get('school-email')
        school_established_date = request.POST.get('school-established-date')
        
        # Extract form data for Chairman (First User)
        chairman_first_name = request.POST.get('chairman-first-name')
        chairman_last_name = request.POST.get('chairman-last-name')
        chairman_email = request.POST.get('chairman-email')
        chairman_password = request.POST.get('chairman-password')
        chairman_phone = request.POST.get('chairman-phone')
        chairman_profile_image = request.FILES.get('chairman-profile-image')

        try:
            with transaction.atomic():
                # Create School
                school = School.objects.create(
                    name=school_name,
                    address=school_address,
                    city=school_city,
                    state=school_state,
                    country=school_country,
                    pincode=school_pincode,
                    email=school_email,
                    establishment_date=school_established_date,
                    website=f"www.{school_name.replace(' ', '').lower()}.com",
                    is_verified=False,
                    is_active=True
                )
                
                # Create Chairman (Superuser)
                chairman = BaseUser.objects.create_superuser(
                    email=chairman_email,
                    username=chairman_email,  # Using email as username
                    password=chairman_password,
                    first_name=chairman_first_name,
                    last_name=chairman_last_name,
                    phone_number=chairman_phone,
                    profile_pic=chairman_profile_image,
                    is_superuser=True,
                    is_staff=True,
                    is_active=True
                )

                # Assign Chairman to School
                school.chairman = chairman.first_name + ' ' + chairman.last_name
                school.save()

            return redirect('schoolloginurl')  # Redirect to login page after successful registration

        except Exception as e:
            return HttpResponse(f"Error occurred: {str(e)}")

    return render(request, 'SchoolRegistration.html')





@csrf_exempt
def schoolloginview(request):
    print("Entered schoolloginview")  # Debug statement

    if request.method == "POST":
        username = request.POST.get("email")  # Get the staff username
        password = request.POST.get("password")  # Get the staff password
        
        print(f"Username: {username}, Password: {password}")

        # Authenticate the user using the username and password
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            # User is authenticated
            print(f"User authenticated: {user}")

            # Log session data before login (optional)
            print(f"Session before login: {request.session.items()}")

            # Manually log in the user
            login(request, user)
            request.session['username'] = username  # Store the username in the session
            print("User logged in successfully.")
            print(f"Session after login: {request.session.items()}")

            # Redirect to the appropriate page (school registration or dashboard)
            return redirect("schoolhomeurl")
        
        else:
            print("Authentication failed: Invalid username or password!")
            messages.error(request, "Invalid username or password!")
            return render(request, "SchoolLogin.html")
    
    print("Request method is not POST. Rendering login page.")
    return render(request, "SchoolLogin.html")





@login_required
# View for schoollogoutpage
def schoollogoutview(request):
    logout(request)
    return redirect('schoolloginurl')

#View for passwordchange
def forgotpasswordview(requests):
    return render(requests, 'ForgotPassword.html')


#View for StudentAdmissionrequests
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
import json
from django.shortcuts import render, get_object_or_404
from Baseuser.models import BaseUser
from django.db import transaction

@login_required
@csrf_protect
def studentadmissionrequestsview(request):
    if request.method == "POST":
        try:
            # Read and decode the incoming JSON data
            data = json.loads(request.body)
            student_id = data.get("id")
            status = data.get("status")

            if not student_id:
                return JsonResponse({"success": False, "error": "Missing student ID"}, status=400)

            # Find the student request by ID
            student_request = get_object_or_404(StudentRegister, id=int(student_id))

            if status == "Approved":
                # Check if the user already exists (to prevent duplicate error)
                if BaseUser.objects.filter(email=student_request.email).exists():
                    return JsonResponse({"success": False, "error": "User already exists"}, status=400)

                # Create BaseUser (Student User)
                user = BaseUser.objects.create(
                    email=student_request.email,
                    first_name=student_request.first_name,
                    last_name=student_request.last_name,
                    phone_number=student_request.phone,
                    password=make_password("defaultpassword"),
                    is_student=True
                )

                # Now, create the Student object linked to the BaseUser instance
                # As Student inherits from BaseUser, the fields from BaseUser will be automatically included
                """student = Student.objects.create(
                    roll_number=student_id,
                    standard=1,  # Default value
                    school=student_request.school,
                    father_name="Unknown",
                    mother_name="Unknown",
                    father_phone="0000000000",
                    mother_phone="0000000000",
                    address=student_request.address,
                    city=student_request.city,
                    state=student_request.state,
                    country=student_request.country,
                    pincode=student_request.pincode,
                    adharcard=student_request.adharcard,
                    tc=student_request.tc,
                    passportphoto=student_request.passportphoto,
                    
                    # Now, link the student data with the created BaseUser fields (inherited fields)
                    #username=user.username,  # For example, if you want to use the username from BaseUser
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    phone_number=user.phone_number,
                )"""

                # Update student request status to "Approved"
                # student_request.status = "Approved"
                #student_request.save(update_fields=["status"])

                return JsonResponse({"success": True})

            elif status == "Rejected":
                #student_request.status = "Rejected"
                #student_request.save(update_fields=["status"])
                return JsonResponse({"success": True})

            return JsonResponse({"success": False, "error": "Invalid status"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON format"}, status=400)
        except Exception as e:
            print(f"Error: {e}")  # Debugging
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    # Handle GET requests
    students = StudentRegister.objects.all()
    return render(request, "student_admission_requests.html", {"students": students})
