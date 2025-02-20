from django.urls import path
from App import views

urlpatterns = [
    path("",views.Landing.as_view(),name="Land"),
    path("Staff/",views.Staff.as_view(),name="Staff"),
    path("Login/",views.Login_page.as_view(),name="Login"),
    path("Home/",views.Home.as_view(),name="Home"),
    path("StudentInfo/",views.StudentInfo.as_view(),name="StudentInfo"),
    path("StudentData/",views.StudentData.as_view(),name="StudentData"),
    path("StaffInfo/",views.StaffInfo.as_view(),name="StaffInfo"),
    path("StaffData/",views.StaffData.as_view(),name="StaffData"),
    path("Logout/",views.LogoutPage.as_view(),name="LogoutPage"),
    path("Team/",views.Team.as_view(),name="Team"),
]