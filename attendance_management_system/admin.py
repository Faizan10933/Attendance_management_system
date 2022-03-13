from django.contrib import admin

from attendance_management_system.models import  Classname, Student, Faculty, Attendance

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Attendance)
admin.site.register(Classname)
# Register your models here.
