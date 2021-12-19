from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

class StudentReadonlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    print(queryset)