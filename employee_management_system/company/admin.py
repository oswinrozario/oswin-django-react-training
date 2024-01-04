from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'industry', 'type', 'active')
    search_fields = ('name', 'location', 'industry')
