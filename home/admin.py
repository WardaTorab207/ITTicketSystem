from django.contrib import admin
from home.models import Employee,Department,Ticket

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','designation','department','dateOfBirth','about','updatedDate','createdDate','IsActive','contact']
    search_field =['name','id']
    actions = ['deleted_selected']
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_field =['name','id']
    actions = ['deleted_selected']
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id','Ticket_des','Ticket_subBy','Ticket_assignTo']
    search_field =['name','id']
    actions = ['deleted_selected']
admin.site.register(Ticket,TicketAdmin)   
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)


# Register your models here.