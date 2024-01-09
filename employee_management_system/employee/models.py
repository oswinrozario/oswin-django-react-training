from django.db import models
from company.models import Company

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('Manager', 'Manager'),
        ('Software Developer', 'Software Developer'),
        ('Project Leader', 'Project Leader'),
    ))
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    company=models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.employee_id}"