from django.db import models

# Create your models here.

class employee_model(models.Model):
    emp_id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    contact_details = models.TextField()
    email = models.EmailField(max_length=100)

    def __str__(self): return self.name

class student_model(models.Model):
    std_id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    contact_details = models.TextField()
    email = models.EmailField(max_length=100)

    def __str__(self): return self.name
