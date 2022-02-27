from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
@api_view()
def hello_world(request):
    return Response({"msg": "Aalekh"})


# send status code by default takes 200 OK status code
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serialzer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"msg": "data saved"})

        return Response(serialzer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "updated"})

        return Response(serializer.errors)


class StudentApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serialzer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"msg": "data saved"})

        return Response(serialzer.errors)

    def put(self, request, format=None):
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "updated"})

        return Response(serializer.errors)
