#editado do zero

#modelando banco de dados

from django.db import models
from uuid import uuid4

#estrutura do banco de dados da app books

# Create your models here.

###def upload_image_book(instance, filename):
###    return f"{instance.id_book}-{filename}"

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=255)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    ###image = models.ImageField(upload_to=upload_image_book, blank=True, null=True)



#do tutorial
#python django + mysql crud api tutorial

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.CharField(max_length=500)
    PhotoFileName = models.CharField(max_length=500)

