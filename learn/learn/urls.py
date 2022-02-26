from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stinfo/<int:pk>', views.student_detail),
    path('stinfo/all', views.student_detail_list)
]
