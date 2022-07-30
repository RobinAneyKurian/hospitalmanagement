from django.db import models
import datetime

# Create your models here.

class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField(null=True)

    def __str__(self):
        return self.dept_name

class Doctors(models.Model):
    doctor_name = models.CharField(max_length=200)
    doc_spec = models.CharField(max_length=200)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_description = models.TextField(null=True)
    doc_img  = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr.' + self.doctor_name + ' - (' + str(self.dep_name) + ')'

class Booking(models.Model):
    patient_name = models.CharField(max_length=150)
    patient_phone = models.IntegerField(null=True)
    patient_email = models.EmailField(null=True)
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField(null=True)
    booked_on = models.DateField(auto_now=True)

class Contact(models.Model):
    hos_con_dept = models.CharField(max_length=150, null=True)
    hos_con_num = models.IntegerField(null=True)


class About(models.Model):
    abt_hos_img = models.ImageField(upload_to = "about")
    abt_hos_description = models.TextField(null=True)

