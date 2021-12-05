from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from .customPermissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
   