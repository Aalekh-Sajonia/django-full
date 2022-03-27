from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)


class JsonPlaceHolderSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    completed = serializers.BooleanField()
