from django.shortcuts import render
from django.http import HttpResponse
from numpy import roll
from .models import Student, Attendance


def attendance_submit(request):
    
    # attendees = request.POST.getlist('present')
    # no_of_attendees = len(attendees)

    # for i in attendees:
    #     s = Student.objects.filter(roll=i)[0]
    #     attendance = Attendance.objects.filter(roll=s)
    #     attendance.current_attendance += 1
    #     attendance.save()
    
    student =  Student.objects.all()
    context={'student': student}
    return render(request, 'markattendance.html', context)


def home(request):
    return render(request, 'index.html')

def teacherhome(request):
    if request.method == "POST":
        # classname = request.POST.get('classname')
        # attend = request.POST.get('present')
        # attendance.attend.a(attend)
        lst=[]
        for c in request.POST.getlist('present'):
            lst.append(c)
        print(lst)
        # Attendance.attend.add(lst)
                # try:
                #     Attendance.objects.get(classname=classname).attend.add(c)
                # except Attendance.DoesNotExist:
                #     classname = None
            # attendance = Attendance(classname=classname, attend=lst)
        attendance = Attendance(attendrecord=lst)
        
        # attendance.attend.set(attend)

        attendance.save()
    
    # student =  Student.objects.all()
    return render(request, 'markattendancehome.html')

def attendance(request):
    if request.method=="POST":
        classname = request.POST.get('classname')
        attend = request.POST.getlist('present')

        attendance = Attendance(classname=classname, attend=attend)

        attendance.save()
    return render(request, 'home.html')




def viewattendance(request):
    return render(request, 'viewattendancehome.html')



def timetable(request):
    return render(request, 'timetablehome.html')


def viewattend(request):
    return render(request, 'viewattendance.html')


def table(request):
    return render(request, 'timetable.html')


# Create your views here.
