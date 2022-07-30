from django.http import HttpResponse
from django.shortcuts import render

from .forms import Bookingform
from .models import Departments, Doctors, Contact, About


# Create your views here.



def index(request):

    numbers = {
        'fruits' : ['Apple', 'Grapes', 'Orange']
    }


    return render(request, "index.html", numbers)


def about(request):

    about_hos = {
        'about_hospital' : About.objects.all()
    }
    return render(request, "about.html", about_hos)


def booking(request):
    if request.method == "POST":
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form =  Bookingform()
    dict_form = {
        'form': form
    }
    return render(request, "booking.html", dict_form)


def doctors(request):

    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, "doctors.html", dict_docs)


def contact(request):

    contact_hos = {
        'con_num': Contact.objects.all
    }
    return render(request, "contact.html", contact_hos)


def department(request):

    dict_dept = {
        'dept' : Departments.objects.all()
    }
    return render(request, "department.html", dict_dept)
