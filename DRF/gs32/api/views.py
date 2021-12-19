from django.db.models import query
from rest_framework import serializers
from rest_framework.throttling import ScopedRateThrottle
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class = [ScopedRateThrottle]
    throttle_scope = 'viewstu' 


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class = [ScopedRateThrottle] 
    throttle_scope = 'modify-stu' 

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class = [ScopedRateThrottle]
    throttle_scope = 'viewstu' 

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class = [ScopedRateThrottle]
    throttle_scope = 'modify-stu' 

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class = [ScopedRateThrottle] 
    throttle_scope = 'modify-stu' 

