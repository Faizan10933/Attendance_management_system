from pydoc import classname
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from numpy import roll
from .models import Classname, Student, Attendance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='/login')
def one(request):
    
    # attendees = request.POST.getlist('present')
    # no_of_attendees = len(attendees)

    # for i in attendees:
    #     s = Student.objects.filter(roll=i)[0]
    #     attendance = Attendance.objects.filter(roll=s)
    #     attendance.current_attendance += 1
    #     attendance.save()
    
    student =  Student.objects.filter(classname=1)
    classname = Classname.objects.filter(classno=1)
    context={'student': student, 'classname': classname}
    return render(request, 'class1.html', context)

@login_required(login_url='/login')
def two(request):
    
    student =  Student.objects.filter(classname=2)
    classname = Classname.objects.filter(classno=2)
    context={'student': student, 'classname': classname}
    return render(request, 'class2.html', context)

@login_required(login_url='/login')
def three(request):
    
    student =  Student.objects.filter(classname=3)
    classname = Classname.objects.filter(classno=3)
    context={'student': student, 'classname': classname}
    return render(request, 'class3.html', context)

@login_required(login_url='/login')
def four(request):
    
    student =  Student.objects.filter(classname=4)
    classname = Classname.objects.filter(classno=4)
    context={'student': student, 'classname': classname}
    return render(request, 'class4.html', context)

@login_required(login_url='/login')
def five(request):
    
    student =  Student.objects.filter(classname=5)
    classname = Classname.objects.filter(classno=5)
    context={'student': student, 'classname': classname}
    return render(request, 'class5.html', context)

@login_required(login_url='/login')
def six(request):
    
    student =  Student.objects.filter(classname=6)
    classname = Classname.objects.filter(classno=6)
    context={'student': student, 'classname': classname}
    return render(request, 'class6.html', context)

@login_required(login_url='/login')
def seven(request):
    
    student =  Student.objects.filter(classname=7)
    classname = Classname.objects.filter(classno=7)
    context={'student': student, 'classname': classname}
    return render(request, 'class7.html', context)

@login_required(login_url='/login')
def eight(request):
    
    student =  Student.objects.filter(classname=8)
    classname = Classname.objects.filter(classno=8)
    context={'student': student, 'classname': classname}
    return render(request, 'class8.html', context)

@login_required(login_url='/login')
def nine(request):
    
    student =  Student.objects.filter(classname=9)
    classname = Classname.objects.filter(classno=9)
    context={'student': student, 'classname': classname}
    return render(request, 'class9.html', context)

@login_required(login_url='/login')
def ten(request):
    
    student =  Student.objects.filter(classname=10)
    classname = Classname.objects.filter(classno=10)
    context={'student': student, 'classname': classname}
    return render(request, 'class10.html', context)




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
        classname = request.POST.get('var')
        print(classname)
        attendance = Attendance(attendrecord=lst, classname=classname, date= datetime.today())
        
        # attendance.attend.set(attend)

        attendance.save()
    
    # student =  Student.objects.all()
    return render(request, 'markattendancehome.html')

@login_required(login_url='/login')
def attendance(request):
    if request.method=="POST":
        classname = request.POST.get('var')
        attend = request.POST.getlist('present')

        attendance = Attendance(classname=classname, attend=attend)
        print(classname)
        attendance.save()
    return render(request, 'home.html')



@login_required(login_url='/login')
def viewattendance(request):
    return render(request, 'viewattendancehome.html')


@login_required(login_url='/login')
def timetable(request):
    return render(request, 'timetablehome.html')

@login_required(login_url='/login')
def viewattend(request, pk):

    classname = Attendance.objects.filter(classname=pk)
    # roll = Attendance.attendrecord.all()
    context={'classname': classname}
    return render(request, 'viewattendance.html', context)

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
