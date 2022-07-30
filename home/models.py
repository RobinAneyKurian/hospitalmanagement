from django.db import models

# Create your models here.

class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField(null=True)

    def __str__(self):
        return self.dept_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_spec = models.CharField(max_length=200)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_description = models.TextField(null=True)
    doc_img  = models.ImageField(upload_to='doctors')