from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(required=False)
    class Meta:
        model = Employee
        fields = '__all__'
