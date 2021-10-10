from django.shortcuts import render


#para habilitar os outros dominios a usar os api methods
from django.views.decorators.csrf import csrf_exempt

#para fazer o parse em json
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

#importar modulos criados
from books.models import Books, Departments, Employees
#from books.models import Books, Lojas, ...
from books.api.serializers import BooksSerializers, DepartmentSerializer, EmployeeSerializer

#adicionando os recursos da foto
from django.core.files.storage import default_storage

# Create your views here.
#por padrao do framework ja tem os metodos implementados
#o codigo a seguir é apenas uma referencia


#aqui estao os metodos para manipular as tabelas
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe = False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data = department_data)
        
        #se os dados forem validos serao salvos no banco de dados
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('adicionado com sucesso', safe = False)
            #safe é mais flexibilidade nas respostas

        return JsonResponse('falha ao adicionar', safe = False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data = department_data)
        
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('atualizacao feita com sucesso', safe = False)
        
        return JsonResponse('falha ao atualizar')

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('deletado com sucesso', safe = False)






#metodos para employess
@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe = False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data = employee_data)
        
        #se os dados forem validos serao salvos no banco de dados
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('adicionado com sucesso', safe = False)
            #safe é mais flexibilidade nas respostas

        return JsonResponse('falha ao adicionar', safe = False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data = employee_data)
        
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('atualizacao feita com sucesso', safe = False)
        
        return JsonResponse('falha ao atualizar')

    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse('deletado com sucesso', safe = False)



@csrf_exempt
def SaveFile(request):
    #acusou o erro na linha abaixo
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)