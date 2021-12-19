from rest_framework import authentication
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
 
   