
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/<int:id>', views.student_api),
    path('student-create', views.student_api_create)
]
