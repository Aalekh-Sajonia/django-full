from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.hello_world),
    path('student/', views.student_api),
    path('student/<int:pk>', views.student_api),
    path('student_class/', views.StudentApi.as_view()),
    path('student_class/<int:pk>', views.StudentApi.as_view()),
    path('student_list_generic/', views.StudentListGeneric.as_view()),
    path('student_list_generic_create/', views.StudentListGenericCreate.as_view()),
    path('student_list_generic_retrieve/<int:pk>', views.StudentListGenericRetrieve.as_view()),
    path('student_list_generic_update/<int:pk>', views.StudentListGenericUpdate.as_view()),
    path('student_list_generic_destroy/<int:pk>', views.StudentListGenericDestroy.as_view())
]
