from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'position', 'date_of_birth', 'date_of_joining','company')
    search_fields = ('full_name', 'email', 'position')
