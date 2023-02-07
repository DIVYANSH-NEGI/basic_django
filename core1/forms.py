from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = student_model
        fields = ['name', 'address', 'contact_details', 'email']

class EmployeeForm(ModelForm):
    class Meta:
        model = employee_model
        fields = ['name', 'address', 'contact_details', 'email']
