from django.db.models import fields
from rest_framework import serializers, validators
from rest_framework.renderers import JSONRenderer
from .models import Student
from datetime import datetime


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    roll = serializers.IntegerField(required= True)
    city = serializers.CharField(max_length=30)

    # class Meta:
    #     validators = [
    #         validators.UniqueTogetherValidator(
    #             queryset = Student.objects.all(),
    #             fields = ['name', 'roll', 'city']
    #         )
    #     ]

    def create(self, validate_data):
        return Student.objects.create(**validate_data)


