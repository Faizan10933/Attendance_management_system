from django.shortcuts import render, redirect
from django.http import HttpResponse
from numpy import roll
from .models import Student, Attendance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def attendance(request):
    if request.method=="POST":
        classname = request.POST.get('classname')
        attend = request.POST.getlist('present')

        attendance = Attendance(classname=classname, attend=attend)

        attendance.save()
    return render(request, 'home.html')



@login_required(login_url='/login')
def viewattendance(request):
    return render(request, 'viewattendancehome.html')


@login_required(login_url='/login')
def timetable(request):
    return render(request, 'timetablehome.html')

@login_required(login_url='/login')
def viewattend(request):
    return render(request, 'viewattendance.html')

@login_required(login_url='/login')
def table(request):
    return render(request, 'timetable.html')


def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password not exists')

    context={'page': page}
    return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


# Create your views here.
