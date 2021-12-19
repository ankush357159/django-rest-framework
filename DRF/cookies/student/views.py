from datetime import datetime, timedelta
from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response =  render(request, 'student/setCookie.html')
    # response.set_cookie('new_name', 'Komal', expires=datetime.utcnow()+timedelta(days=2))
    response.set_signed_cookie('name', 'Gita', salt="asdf", expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name', "Guest")
    name = request.get_signed_cookie('name', default="Guest", salt="asdf")
    # If cookie name does not exist, Guest name will be set


    return render(request, 'student/getCookie.html', {'name': name})

def deletecookie(request):
    response = render(request, 'student/deleteCookie.html')
    response.delete_cookie('name')
    return response
