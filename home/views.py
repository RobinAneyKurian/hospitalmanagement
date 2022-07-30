from django.http import HttpResponse
from django.shortcuts import render
from .models import Departments

# Create your views here.



def index(request):

    numbers = {
        'fruits' : ['Apple', 'Grapes', 'Orange']
    }


    return render(request, "index.html", numbers)


def about(request):
    return render(request, "about.html")


def booking(request):
    return render(request, "booking.html")


def doctors(request):
    return render(request, "doctors.html")


def contact(request):
    return render(request, "contact.html")


def department(request):

    dict_dept = {
        'dept' : Departments.objects.all()
    }
    return render(request, "department.html", dict_dept)
