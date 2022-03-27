from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)


# Filter backends set at global level
class StudentListDjangoFilter(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['city', 'name']
