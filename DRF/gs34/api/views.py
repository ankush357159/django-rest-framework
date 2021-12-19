from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='new_user1')
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    filterset_fields = ['name', 'city']
    # Two filters can be combined together

    def get_queryset(self):
        user = self.request.user
        return  Student.objects.filter(passby=user)

