from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Employee
from .serializers import Employeeserializer,Companyserializer
# Create your views here.
from .permission import isADMinOrReadonly
class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=Companyserializer
    permission_classes=isADMinOrReadonly
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer
    permission_classes=isADMinOrReadonly

