from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.http import JsonResponse
from home.models import Ticket, Item,Employee,Department
import datetime

# Create your views here.

# username = user
# password = User123!@#
# This code if for index page
allEmployee = Employee.objects.all()

def index(request):
    if request.user.is_anonymous:
       return redirect("/login")
    id = request.session.get('id')
    return render(request, 'index.html')
 
def emp_tickets(request):
    id = request.session.get('id')
    print(id)
    employee = Employee.objects.get(id=id)
    print("YOUR ID S ---------------",id)
    employee_name = employee.name
    print(employee_name)
    allTicket = Ticket.objects.filter(Ticket_assignTo=employee_name).order_by('-id')
    print(allTicket)
    context = {"allTicket" : allTicket}
    return render(request, 'emp_tickets.html',context) 

def add_ticket(request):
    isManager =  request.session.get('is_manager')
    allEmployee = Employee.objects.all()
    project_list = ('5S System', 'Automations', 'Bar Stock Inventory Audit','Calibration','Costing','Dashboard - Main','Time Clock','HR - Human Resources','Toolcrib','Surveillance','SetupSheet','StockRoom','Quality','Production','Metrics','Maintence')
    context = {"project_list": project_list,"allEmployee" : allEmployee}
    
    if request.method == "POST":
        print("This is the post")
        desc = request.POST['ticket_description']
        type = request.POST['Type']
        urgency = request.POST['Urgency']
        assignEmp = request.POST['asgEmp']
        subEmp = request.POST['SubEmp']
        project = request.POST['Project']
        
        ins = Ticket(
            Ticket_des=desc,
            Ticket_assignTo=assignEmp,
            Ticket_subBy=subEmp,
            Ticket_type=type,
            Ticket_project=project,
            Ticket_urgency=urgency,
            Ticket_openDate=datetime.datetime.now()
        )
        ins.save()
        messages.success(request, "Ticket has been added successfully!")
   
    return render(request, 'addTicket.html', context)

def employee_profile(request):
    id = request.session.get('id')
    print("YOUR ID S ---------------",id)
    employee = Employee.objects.get(id=id)
    employee_Data = {
        "id" : employee.id,
        "name" : employee.name,
        "dateOfBirth" : employee.dateOfBirth,
        "about" : employee.about,
        "contact" : employee.contact,
        "department" : employee.department,
        "designation" : employee.designation,
        "email" : employee.email,
        "password": employee.password
    }
    print(employee_Data)
    return render(request, 'profile.html',employee_Data)


def loginpage(request):
    allEmployee = Employee.objects.all()
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username= username, password= password)
        Islogin = False
        print(username, password)
        for employee in allEmployee:
            print("Employee =",employee.name,"  ",employee.password)
            if username == employee.name and password == employee.password:
                Islogin = True
                isManager = employee.IsManager
                EmpId = employee.id

        print(Islogin)
        if Islogin == True:
            request.session['id'] = EmpId
            print("YOUR ID S ---------------",EmpId)
            print(employee.id , employee.name)
            messages.success(request, "Login succuessfully.")
            if isManager == True :
                request.session['is_manager'] = True
                return render(request, 'admin/adminIndex.html')
            else:
                return render(request, 'index.html')
        else:
            
            # No backend authenticated the credentials
            messages.error(request, "Incorrect username or password.")
            return render(request, 'index.html')

    return render(request, 'loginForm.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def updateProfile(request):
    id = request.session.get('id')
    print(id)
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        designation = request.POST['designation']
        password = request.POST['password']
        about = request.POST['about']
        contact = request.POST['contact']
        
        employee.name = name
        employee.email = email
        employee.designation = designation
        employee.department = employee.department
        employee.password = password
        employee.about = about
        employee.contact = contact
        employee.gender = employee.gender
        employee.Post = employee.Post
        employee.dateOfBirth = employee.dateOfBirth
        employee.createdDate = employee.createdDate
        employee.updatedDate = datetime.datetime.now()
        employee.IsActive = True
        employee.IsManager = employee.IsManager
        print(employee)
        employee.save()
        messages.success(request, "Employee has been Updated successfully!")

        return render(request, 'profile.html')

# Admin Section View.py 

def indexAdmin(request):
    if request.user.is_anonymous:
       return redirect("/login")
    id = request.session.get('id')
    return render(request, 'admin/adminIndex.html')



def admin_add_ticket(request):
    project_list = ['5S System', 'Automations', 'Bar Stock Inventory Audit','Calibration','Costing','Dashboard - Main','Time Clock','HR - Human Resources','Toolcrib','Surveillance','SetupSheet','StockRoom','Quality','Production','Metrics','Maintence']
    context = {"project_list": project_list,"allEmployee" : allEmployee}
    
    if request.method == "POST":
        print("This is the post")
        desc = request.POST['ticket_description']
        type = request.POST['Type']
        urgency = request.POST['Urgency']
        assignEmp = request.POST['asgEmp']
        subEmp = request.POST['SubEmp']
        project = request.POST['Project']
        
        ins = Ticket(
            Ticket_des=desc,
            Ticket_assignTo=assignEmp,
            Ticket_subBy=subEmp,
            Ticket_type=type,
            Ticket_urgency=urgency,
            Ticket_openDate=datetime.datetime.now()
        )
        ins.save()
        messages.success(request, "Ticket has been added successfully!")
    
    return render(request, 'admin/admin_addTicket.html', context)


def all_tickets(request):
    allTicket = Ticket.objects.all().order_by('-id')
    context = {"allTicket" : allTicket}
    return render(request, 'admin/all_tickets.html',context)


def add_employee(request):
    post_list=['CEO (Chief Executive Officer)','CFO (Chief Financial Officer)','CTO (Chief Technology Officer)','COO (Chief Operating Officer)','CMO (Chief Marketing Officer)','HR Manager (Human Resources Manager)','Graphic Designer','Software Engineer','Administrative Assistant','Project Manager','IT Manager','Executive Assistant','Data Analyst','Training Coordinator','Business Development Executive','IT Support Technician','Research Analyst','Customer Service Associate','Sales Representative']
    gender_list = ['Male','Female']
    all_Department = Department.objects.all().order_by('-id')
    print(all_Department)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        emp_post = request.POST['post']
        gender = request.POST['gender']
        password = request.POST['password']
        designation = request.POST['designation']
        department = request.POST['department']
        about = request.POST['about']
        contact = request.POST['contact']
        DateOfBirth = request.POST['birthday']
        print(name,email,password,designation,department,about,contact,DateOfBirth)
        employee = Employee(
            name=name,
            email=email,
            gender=gender,
            Post=emp_post,
            password=password,
            designation=designation,
            department=department,
            dateOfBirth=DateOfBirth,
            about=about,
            contact=contact,
            IsActive=True,
            createdDate=datetime.datetime.now,
        )
        employee.save()
        messages.success(request, "Employee has been added successfully!")
    
    context = {"post_list":post_list,"gender_list":gender_list,"allDepartment":all_Department}
    return render(request, 'admin/addEmployee.html',context)

def all_employees(request):
    allEmployee = Employee.objects.all().order_by('-id')
    context = {"allEmployee" : allEmployee}
    return render(request, 'admin/all_employees.html',context)

def update_value(request):
    if request.method == 'POST':
        object_id = request.POST['object_id']
        try:
            obj = Ticket.objects.get(id=object_id)
            # Toggle the boolean value
            obj.Ticket_isComplete = True
            obj.save()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Object not found.'})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def update_approve_value(request):
    if request.method == 'POST':
        object_id = request.POST['object_id']
        try:
            obj = Ticket.objects.get(id=object_id)
            # Toggle the boolean value
            obj.Ticket_isApprove = True
            obj.save()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Object not found.'})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def update_reject_value(request):
    if request.method == 'POST':
        object_id = request.POST['object_id']
        try:
            obj = Ticket.objects.get(id=object_id)
            # Toggle the boolean value
            obj.Ticket_isApprove = False
            obj.save()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Object not found.'})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


def delete_item(request, item_id):
    item = get_object_or_404(Ticket, id=item_id)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Ticket has been deleted successfully!")
        return redirect('/admin-allTickets')
    
    return render(request, 'confrim_del.html', {'item': item})

def delete_emp(request, emp_id):
    item = get_object_or_404(Employee, id=emp_id)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Employee has been deleted successfully!")
        return redirect('/admin-allEmployees')
    
    return render(request, 'confrim_del.html', {'item': item})
