from django.shortcuts import render

from .myPagination import MyPageNumberPagination
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination

