import pytest
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch, Mock
from company.models import Company
from account.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
@patch('account.views.RefreshToken.for_user')
def test_user_registration_view(mock_for_user):
    client = APIClient()
    company = Company.objects.create(name='Test Company')
    response = client.post(
        '/api/register/',
        data={
            'username': 'new_user',
            'email': 'new_user@example.com',
            'password': 'password',
            'company': company.pk,
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert 'user_id' in response.data
    assert 'access_token' in response.data
    assert 'refresh_token' in response.data
