from rest_framework import serializers
from .models import Employee,Department

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')

class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('__all__')
