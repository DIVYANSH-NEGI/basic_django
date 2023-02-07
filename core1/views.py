from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here

def index(request):
    return render(request,'index.html')


def EmployeeCreate(request):
    form = EmployeeForm()
    if request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
               'form':form
               }
    return render(request,'createEmp.html',context)

def StudentCreate(request):
    form = StudentForm()
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
               'form':form
               }
    return render(request,'createStd.html',context)
