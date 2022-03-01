from django.contrib import admin
from django.urls import path
from api import views
from rest_framework import routers
from django.conf.urls import include

rr = routers.DefaultRouter()

rr.register('studentapi', views.StudentModelViewSet, basename='studentapi' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(rr.urls)),
    path('test/', views.hello_world),
    path('student/', views.student_api),
    path('student/<int:pk>', views.student_api),
    path('student_class/', views.StudentApi.as_view()),
    path('student_class/<int:pk>', views.StudentApi.as_view()),
    path('student_list_generic/', views.StudentListGeneric.as_view()),
    path('student_list_generic_create/', views.StudentListGenericCreate.as_view()),
    path('student_list_generic_retrieve/<int:pk>', views.StudentListGenericRetrieve.as_view()),
    path('student_list_generic_update/<int:pk>', views.StudentListGenericUpdate.as_view()),
    path('student_list_generic_destroy/<int:pk>', views.StudentListGenericDestroy.as_view()),
    path('student_list_concrete/', views.StudentListConcrete.as_view()),
    path('student_create_concrete/', views.StudentCreateConcrete.as_view()),
    path('student_retrieve_concrete/<int:pk>', views.StudentRetrieveConcrete.as_view()),
    path('student_update_concrete/<int:pk>', views.StudentUpdateConcrete.as_view()),
    path('student_destroy_concrete/<int:pk>', views.StudentDestroyConcrete.as_view())
]
