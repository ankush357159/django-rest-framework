from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='new_user1')
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        return  Student.objects.filter(passby=user)

