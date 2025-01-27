from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, employee  # Ensure the model name 'employee' is lowercase if that's how it's defined
from api.serializers import CompanySerializer, EnployeeSerialiser  # Keep the serializer naming as it is
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # companies/{companyId}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = Company.objects.get(pk=pk)  # Fetch the company by primary key
        emps = employee.objects.filter(company=company)  # Filter employees by company
        # Correct the context syntax: use {'request': request} instead of {'request:request'}
        emp_serializer = EnployeeSerialiser(emps, many=True, context={'request': request})
        return Response(emp_serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EnployeeSerialiser
