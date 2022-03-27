import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer, JsonPlaceHolderSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.
@csrf_exempt
def student_create(request):
    # calling 3rd party api service
    if request.method == 'GET':
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        pyData = JsonPlaceHolderSerializer(response.json())
        json_data = JSONRenderer().render(pyData.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
