import pytest
from unittest.mock import patch
from django.db import models
from company.models import Company

@patch('company.models.Company.objects.create')
def test_company_model(mock_create):
    mock_company = Company(
        name='Test Company',
        location='Test Location',
        industry='Technology',
        website='http://example.com',
        about='Test about',
        type='Technology',
        revenue=1000000.50,
        employees_count=100,
        founded_date='2022-01-01',
        active=True
    )
    mock_create.return_value = mock_company
    created_company = Company.objects.create(
        name='Test Company',
        location='Test Location',
        industry='Technology',
        website='http://example.com',
        about='Test about',
        type='Technology',
        revenue=1000000.50,
        employees_count=100,
        founded_date='2022-01-01',
        active=True
    )
    assert created_company == mock_company
    mock_create.assert_called_once_with(
        name='Test Company',
        location='Test Location',
        industry='Technology',
        website='http://example.com',
        about='Test about',
        type='Technology',
        revenue=1000000.50,
        employees_count=100,
        founded_date='2022-01-01',
        active=True
    )
