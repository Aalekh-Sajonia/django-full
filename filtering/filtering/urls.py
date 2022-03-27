from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    path('studentapi_filter/', views.StudentListDjangoFilter.as_view()),
    path('studentapi_search_filter', views.StudentListSearchFilter.as_view()),
    path('studentapi_ordering_filter', views.StudentListOrderingFilter.as_view())
]
