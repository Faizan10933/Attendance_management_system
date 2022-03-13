
from . import views
from django.urls import path

urlpatterns = [
    path('attendance_submit', views.attendance_submit, name="attendance_submit"),
    path('', views.home, name="home")

]