from unittest import mock
import pytest
from rest_framework.test import APIClient
from unittest.mock import Mock, patch
from company.models import Company
from company.serializers import CompanySerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def company_data():
    return {
        'name': 'Test Company',
        'location': 'Test Location',
        'industry': 'Technology',
        'website': 'http://example.com',
        'about': 'Test about',
        'type': 'Technology',
        'revenue': 1000000.00,  # Corrected to use decimal
        'employees_count': 100,
        'founded_date': '2022-01-01',
        'active': True
    }

@mock.patch.object(Company.objects, 'create')
@pytest.mark.django_db
def test_create_company(mock_create, api_client, company_data):
    mock_company = Company(**company_data)
    mock_create.return_value = mock_company
    response = api_client.post('/api/companies/', data=company_data, format='json')
    assert response.status_code == 201
    assert response.data == CompanySerializer(mock_company).data
    mock_create.assert_called_once()
    