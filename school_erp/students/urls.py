from django.urls import path
from students.views import homepageview, registrationview, loginview


urlpatterns = [
    path('studenthome/', homepageview, name='studenthomeurl'),
    path('studentregistration/', registrationview, name='studentregisterurl'),
    path('studentlogin/', loginview, name='studentloginurl'),
    
]