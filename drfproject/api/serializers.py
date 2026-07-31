from rest_framework import serializers
from .models import Company,Employee

class Employeeserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Employee
        fields='__all__'
        
class Companyserializer(serializers.ModelSerializer):
    employees=Employeeserializer(many=True,read_only=True)
    class Meta:
        model=Company
        fields='__all__'