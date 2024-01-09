from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    about = models.TextField()
    COMPANY_TYPES = [
        ('Technology', 'Technology'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Manufacturing', 'Manufacturing'),
        ('Retail', 'Retail'),
        ('Telecommunications', 'Telecommunications'),
    ]
    type = models.CharField(max_length=100, choices=COMPANY_TYPES)
    revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    employees_count = models.PositiveIntegerField(null=True, blank=True)
    founded_date = models.DateField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
