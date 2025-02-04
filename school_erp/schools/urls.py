from django.urls import path
from schools.views import schoolhomeview, schoolloginview, schoollogoutview, schoolregisterview, forgotpasswordview, studentadmissionrequestsview

urlpatterns = [
    path('schoolhome/',schoolhomeview, name="schoolhomeurl"),
    path('schoollogin/',schoolloginview, name="schoolloginurl"),
    path('schoollogout/',schoollogoutview, name="schoollogouturl"),
    path('schoolregister/',schoolregisterview, name="schoolregisterurl"),
    path('resetpassword/',forgotpasswordview, name="resetpasswordurl"),
    path('studentsadmissionrequests/',studentadmissionrequestsview, name="studentadmissionrequestsurl"),
    # Include other app URLs here
]
