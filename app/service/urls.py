from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('api/teacher/<int:pk>/', views.api_teacher_detail),
    path('api/teacher/', views.api_teacher),
    path('api/webinar/<int:pk>/', views.api_webinar_detail),
    path('api/webinar/', views.api_webinar),
    path('api/course/<int:pk>/', views.api_course_detail),
    path('api/course/', views.api_course),
    path('api/calculate_salary/<int:pk>/', views.api_calculate_salary)
]
