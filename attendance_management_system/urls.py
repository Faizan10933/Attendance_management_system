
from . import views
from django.urls import path

urlpatterns = [
    path('attendance_submit', views.attendance_submit, name="attendance_submit"),
    path('', views.home, name="home"),
    path('teacherhome',views.teacherhome, name="teacherhome"),
    path('viewattendance',views.viewattendance, name="viewattendance"),
    path('viewattend',views.viewattend, name="viewattend"),
    path('timetable',views.timetable, name="timetable"),
    path('table',views.table, name="table"),

]