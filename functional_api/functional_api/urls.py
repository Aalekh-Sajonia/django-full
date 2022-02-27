from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.hello_world),
    path('student/', views.student_api),
    path('student/<int:pk>', views.student_api)
]