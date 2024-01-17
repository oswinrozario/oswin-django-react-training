import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from unittest.mock import patch
from account.models import CustomUser
from company.models import Company

@pytest.fixture
def company():
    return Company.objects.create(name='Test Company')

@pytest.mark.django_db
def test_custom_user_creation(company):
    user = get_user_model().objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='password',
        company=company,
    )

    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert user.company == company
    assert str(user) == 'testuser'

@pytest.mark.django_db
# patch is a way to implement mocking, here we are mocking the create_user method
@patch.object(get_user_model().objects, 'create_user')
def test_custom_user_creation_with_mock(mock_create_user, company):
    mock_create_user.return_value = CustomUser(
        username='mockuser',
        email='mockuser@example.com',
        password='password',
        company=company,
    )

    user = CustomUser.objects.create_user(
        username='mockuser',
        email='mockuser@example.com',
        password='password',
        company=company,
    )

    assert user.username == 'mockuser'
    assert user.email == 'mockuser@example.com'
    assert user.company == company
    assert str(user) == 'mockuser'
    mock_create_user.assert_called_once_with(
        username='mockuser',
        email='mockuser@example.com',
        password='password',
        company=company,
    )

@pytest.mark.django_db
@patch.object(get_user_model().objects, 'create_user')
def test_custom_user_creation_invalid_email_with_mock(mock_create_user, company):
    mock_create_user.side_effect = ValidationError('Enter a valid email address.')
    with pytest.raises(ValidationError, match='Enter a valid email address.'):
        CustomUser.objects.create_user(
            username='testuser',
            email='invalid-email',
            password='password',
            company=company,
        )
