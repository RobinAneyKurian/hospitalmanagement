from django.db import models

# Create your models here.

class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()