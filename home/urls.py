from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emp_tickets/', views.emp_tickets, name='emp_tickets'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.employee_profile, name='employeeProfile'),
    path('profile/update/', views.updateProfile, name='update_profile'),
    path('add-ticket/', views.add_ticket, name='addTicket'),

    # admin paths
    path('admin-desboard/', views.indexAdmin, name='admin-desboard'),
    path('admin-addEmployee/', views.add_employee, name='admin-addEmployee'),
    path('admin-allTickets/', views.all_tickets, name='admin-allTickets'),
    path('admin-addTicket/', views.admin_add_ticket, name='admin-addTicket'),
    path('admin-allEmployees/', views.all_employees, name='admin-allEmployees'),
    path('update-value/', views.update_value, name='update_value'),
    path('update-approve-value/', views.update_approve_value, name='update-approve-value'), 
    path('update-reject-value/', views.update_reject_value, name='update-reject-value'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete-item'),
    path('delete-emp/<int:emp_id>/', views.delete_emp, name='delete-emp'),
     
    
]


