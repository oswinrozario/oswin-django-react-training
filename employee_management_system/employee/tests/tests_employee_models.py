import pytest
from django.db import IntegrityError
from django.utils import timezone
from company.models import Company
from employee.models import Employee
from unittest.mock import patch, MagicMock

@pytest.fixture
def sample_company():
    return Company.objects.create(
        name='Sample Company',
        location='Sample Location',
        industry='Sample Industry',
        type='Technology',
        about='Sample about',
        revenue=1000000,
        employees_count=50,
        founded_date=timezone.now().date()
    )

@pytest.fixture
def sample_employee(sample_company):
    return Employee.objects.create(
        full_name='John Doe',
        email='john.doe@example.com',
        address='123 Main St',
        phone='123-456-7890',
        about='Employee about',
        position='Software Developer',
        date_of_birth=timezone.now().date(),
        date_of_joining=timezone.now().date(),
        company=sample_company
    )

@pytest.mark.django_db
@patch('employee.models.Employee.__str__')
def test_employee_mock_company(mock_str, sample_employee):
    mock_str.return_value = f"Mocked Employee - {sample_employee.id}"

    expected_str = f"Mocked Employee - {sample_employee.id}"
    assert str(sample_employee) == expected_str
