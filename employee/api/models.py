from django.db import models

class Department(models.Model):
    departmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.departmentName




class Employee(models.Model):
    empName = models.CharField(max_length=100)
    empAge = models.IntegerField()
    empDepartment = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) :
        return self.empName
    
