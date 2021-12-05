from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


# Creating router object
router = DefaultRouter()

# Register StudentViewset with Router
router.register('studentapi', views.StudentReadonlyViewSet, basename='student')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
