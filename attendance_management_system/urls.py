
from . import views
from django.urls import path

urlpatterns = [
    # path('attendance_submit', views.attendance_submit, name="attendance_submit"),
    path('', views.home, name="home"),
    path('teacherhome',views.teacherhome, name="teacherhome"),
    path('viewattendance',views.viewattendance, name="viewattendance"),
    path('viewattend/<str:pk>/',views.viewattend, name="viewattend"),
    path('timetable',views.timetable, name="timetable"),
    path('table',views.table, name="table"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('one/', views.one, name="one"),
    path('two/', views.two, name="two"),
    
    path('three/', views.three, name="three"),
    path('four/', views.four, name="four"),
    path('five/', views.five, name="five"),
    path('six/', views.six, name="six"),
    path('seven/', views.seven, name="seven"),
    path('eight/', views.eight, name="eight"),
    path('nine/', views.nine, name="nine"),
    path('ten/', views.ten, name="ten"),

]