from django.db import models

# Create your models here.
class Ticket(models.Model):
    Ticket_des= models.TextField()
    Ticket_subBy = models.CharField(max_length=50)
    Ticket_assignTo = models.CharField(max_length=100)
    Ticket_type = models.CharField(max_length=30)
    Ticket_urgency = models.CharField(max_length=30)
    Ticket_project = models.CharField(max_length=50)
    Ticket_openDate = models.DateField(verbose_name=("Open date"), auto_now_add=True, null=True)
    Ticket_isApprove = models.BooleanField(null=True)
    Ticket_isComplete = models.BooleanField(default=False)
    Ticket_closedDate = models.DateField(verbose_name=("Closed date"), auto_now_add=False, null=True)
    Ticket_UpdatedDate= models.DateField(verbose_name=("Updated date"), auto_now_add=False, null=True)


class Item(models.Model):
    description = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.description
    
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    Post = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    department = models.CharField(max_length=30)
    designation = models.CharField(max_length=100)
    dateOfBirth = models.DateTimeField(verbose_name=("Date of Birth"), auto_now_add=False, null=True)
    about = models.TextField()
    createdDate = models.DateTimeField(verbose_name=("Created date"), auto_now_add=True, null=True)
    updatedDate = models.DateTimeField(verbose_name=("Updated date"), auto_now_add=False, null=True)
    IsActive = models.BooleanField(default=True)
    IsManager = models.BooleanField(default=True)
    contact = models.CharField(max_length=11)

    

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    createdDate = models.DateTimeField(verbose_name=("Created date"), auto_now_add=True, null=True)
    updatedDate = models.DateTimeField(verbose_name=("Updated date"), auto_now_add=False, null=True)
    
    def __str__(self):
        return self.name
    