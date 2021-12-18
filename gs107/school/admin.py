from django.contrib import admin
from .models import ProxyStudent, Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name']

@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name']
