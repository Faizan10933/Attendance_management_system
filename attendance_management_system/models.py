from msilib.schema import Class
from pickle import TRUE
from pyexpat import model
from django.db import models
from numpy import number, roll
from django.contrib.auth.models import User



class Classname(models.Model):
    classno = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.classno


class Student(models.Model):
    
    roll = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=40, null=False, default='')
    classname = models.ForeignKey('Classname', on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=False, default='')
    parent_phone = models.CharField(max_length=12, null=False, default='')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    classname = models.CharField(max_length=40, default=None)
    attendrecord = models.CharField(max_length=40, default=None)
    date = models.DateField(default=None)
   
    def __str___(self):
        return self.date


class Faculty(models.Model):
    faculty = models.OneToOneField(to=User, on_delete=models.CASCADE)
    faculty_name = models.CharField(max_length=40)
    classname = models.ForeignKey('Classname', on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=10)

    def __str__(self):
        return self.faculty_name