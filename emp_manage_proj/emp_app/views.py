from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request , "home.html")

def view_emp(request):
    emps = Employee.objects.all()   # to view all items in model
    context = {
        'emps': emps
    }
    return render(request , "view_emp.html", context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        dept = int(request.POST["dept"])
        role = int(request.POST["role"])
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])
        phone_no = int(request.POST["phone_no"])

        new_employee = Employee(first_name=first_name, last_name=last_name, dept_id=dept, role_id=role, salary=salary, bonus=bonus, phone_no=phone_no, hiring_date=datetime.now())
        new_employee.save()
        return HttpResponse("Employee Added Successfully!!!")
    elif request.method == "GET":
        return render(request , "add_emp.html")
    else:
        return HttpResponse("Employee Not Added!!!")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!!!")
        except:
            return HttpResponse("Enter a Valid emp_id!!!")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request , "remove_emp.html", context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context = {
            'emps': emps
        }
        return render(request, "view_emp.html", context)
    elif request.method == "GET":
        return render(request , "filter_emp.html")
    else:
        return HttpResponse("An Exception Occured!!!")
