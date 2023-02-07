from django.urls import path
from .import views
urlpatterns=[
    path("",views.index,name="index"),
    path("createEmp",views.EmployeeCreate,name="emp-create"),
    path("createStd",views.StudentCreate,name="std-create"),
]
