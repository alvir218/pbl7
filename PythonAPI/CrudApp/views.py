from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CrudApp.models import Editora, Livro, EditoraLivro
from CrudApp.serializers import EditoraSerializer, LivroSerializer, EditoraLivroSerializer


# Create your views here.
@csrf_exempt
def EditoraApi(request, id=0):
    if request.method == 'GET':
        editora = Editora.objects.all()
        editora_serializer = EditoraSerializer(editora, many=True)
        return JsonResponse(editora_serializer.data, safe=False)
    elif request.method == 'POST':
        editora_data = JSONParser().parse(request)
        editora_serializer = EditoraSerializer(data=editora_data)
        if editora_serializer.is_valid():
            editora_serializer.save()
            return JsonResponse("Salvo com sucesso", safe=False)
        return JsonResponse("Falha ao salvar a requisição", safe=False)
    elif request.method == 'PUT':
        editora_data = JSONParser().parse(request)
        editora = Editora.objects.get(EditoraId=editora_data['EditoraId'])
        editora_serializer = EditoraSerializer(editora, data=editora_data)
        if editora_serializer.is_valid():
            editora_serializer.save()
            return JsonResponse("Salvo com sucesso", safe=False)
        return JsonResponse("Falha ao salvar a requisição", safe=False)
    elif request.method == 'DELETE':
        editora = Editora.objects.get(EditoraId=id)
        editora.delete()
        return JsonResponse("Excluído com sucesso", safe=False)
