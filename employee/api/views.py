from django.shortcuts import render
from rest_framework import generics

from .models import Department,Employee
from .serializers import Employeeserializer,Departmentserializer


class EmpList(generics.ListCreateAPIView):
    serializer_class = Employeeserializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department')
        if department is not None:
            queryset = queryset.filter(empDepartment=department)
        return queryset


class EmpDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Employeeserializer
    queryset = Employee.objects.all()

class DpmntList(generics.ListCreateAPIView):
    serializer_class = Departmentserializer
    queryset = Department.objects.all()

class DpmntDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Departmentserializer
    queryset = Department.objects.all()


