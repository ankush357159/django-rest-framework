from django.db import models

from school.managers import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    # objects = models.Manager() --> thi is the default instance of Manager interface
    objects = models.Manager()
    students = CustomManager()

class ProxyStudent(Student):
    students = CustomManager()
    class Meta:
        proxy=True
        ordering = ['name']
