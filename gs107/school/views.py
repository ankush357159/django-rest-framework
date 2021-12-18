from django.shortcuts import render
from .models import ProxyStudent, Student

# Create your views here.
def home(request):
    # student_data = Student.students.all()
    # student_data = Student.objects.all()
    # student_data = Student.students.get_stu_roll_range(101,105)
    student_data = ProxyStudent.students.get_stu_roll_range(103,109).order_by('id')
    return render(request, 'school/home.html', {'students':student_data})
