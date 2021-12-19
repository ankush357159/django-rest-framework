from rest_framework import authentication
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from api.customAuth import CustomAuthentication
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
   