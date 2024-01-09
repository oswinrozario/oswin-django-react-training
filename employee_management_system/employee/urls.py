from django.urls import path, include
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
]