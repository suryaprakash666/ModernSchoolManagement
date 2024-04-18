from django.urls import path, include
from rest_framework import routers
from .Views import Staffhomepage, DataTableView, HomepageView, StaffLoginView, StaffRegisterView, StudentRegisterView, \
    SchoolRegisterView, SchoolSignView, GradingTabView, StudentLoginView, SchoolLoginView
from .Views.apiviews import Dataviewset, Staffdataviewset, Studentdataviewset

router = routers.DefaultRouter()
router.register(r'school', Dataviewset)
router.register(r'staff', Staffdataviewset)
router.register(r'student', Studentdataviewset)

urlpatterns = [
    # WebsiteRelatedURLs
    path('api/', include(router.urls)),
    path('', HomepageView.homepageview, name="Homepage"),

    # StaffRelatedURLs
    path('staffview/', Staffhomepage.staffhomeview, name="Staffhome"),
    path('stafflogin/', StaffLoginView.staffloginview, name="Stafflogin"),
    path('staffregister/', StaffRegisterView.staffregisterview, name="Staffregisterlink"),
    path('gradingtab', GradingTabView.gradingtabview, name="gradingtaburl"),
    path('sendmessage/', Staffhomepage.send_whatsapp_message, name="Sendmessage"),

    # StudentRelatedURLs
    path('studentlogin/', StudentLoginView.studentloginview, name="gradingtaburl"),
    path('studentregister/', StudentRegisterView.studentregisterview, name="Studentregisterlink"),

    # SchoolRelatedURLs
    path('schoolregister/', SchoolRegisterView.schoolregisterview, name="schoolregisterlink"),
    path('schoollogin/', SchoolLoginView.schoolloginview, name="schoolloginlink")

]
