from atexit import register
from pydoc import Doc
from django.contrib import admin
from .models import Departments
from .models import Doctors

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)