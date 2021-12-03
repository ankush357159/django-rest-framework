from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, unique=True)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)
