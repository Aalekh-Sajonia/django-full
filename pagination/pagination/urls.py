from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    path('studentapi_limit_offset/', views.StudentListLimitOffset.as_view()),
    path('studentapi_cursor/', views.StudentListCursor.as_view()),
]
