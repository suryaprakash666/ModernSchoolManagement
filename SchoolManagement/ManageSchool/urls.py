from django.urls import path, include
from rest_framework import routers

from .Views import Staffhomepage, HomepageView, StaffLoginView, StaffRegisterView, StudentRegisterView, \
    SchoolRegisterView, GradingTabView, StudentLoginView, SchoolLoginView, Studenthomepage, SchoolHomeview, \
    staffnavbarview
from .Views.SchoolHomeview import student_requests_tabview, teacher_requests_tabview
from .Views.apiviews import Schooldataviewset, Staffdataviewset, Studentdataviewset, \
    Classdataviewset, SubjectViewset
from .Views.clearCacheView import clear_cache_view

router = routers.DefaultRouter()
router.register(r'school', Schooldataviewset)
router.register(r'staff', Staffdataviewset)
router.register(r'student', Studentdataviewset)
router.register(r'studentclass', Classdataviewset)
router.register(r'subject', SubjectViewset)

urlpatterns = [
    # WebsiteRelatedURLs
    path('api/', include(router.urls)),
    path('', HomepageView.homepageview, name="Homepage"),

    # StaffRelatedURLs
    path('staffview/', Staffhomepage.staffhomeview, name="Staffhome"),
    path('stafflogin/', StaffLoginView.staffloginview, name="Stafflogin"),
    path('staffregister/', StaffRegisterView.staffregisterview, name="Staffregisterlink"),
    path('gradingtab', GradingTabView.gradingtabview, name="gradingtaburl"),
    path('staffnavbar/', staffnavbarview.staffnavbarview, name="staffnavbar"),

    # StudentRelatedURLs
    path('studentlogin/', StudentLoginView.studentloginview, name="studentloginurl"),
    path('studentregister/', StudentRegisterView.studentregisterview, name="Studentregisterlink"),
    path('studenthome/', Studenthomepage.studenthomeview, name="studenthomeurl"),

    # SchoolRelatedURLs
    path('schoolregister/', SchoolRegisterView.schoolregisterview, name="schoolregisterlink"),
    path('schoollogin/', SchoolLoginView.schoolloginview, name="schoolloginlink"),
    path('schoolhome/', SchoolHomeview.schoolhomeview, name="schoolhomeurl"),
    path('studentrequesttab', student_requests_tabview, name="student_requests_tabview"),
    path('teacherrequesttab', teacher_requests_tabview, name="teacher_requests_tabview"),

    # other urls
    path('clearcache/', clear_cache_view, name="clearcache"),

]
