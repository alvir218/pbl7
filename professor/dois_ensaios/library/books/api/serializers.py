from rest_framework import serializers
#from books import models
from books.models import Books, Departments, Employees


class BooksSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = '__all__'

        #pode ser escolhido os campos a serem usados
        #fields=(entidade1, entidade2)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId', 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')
