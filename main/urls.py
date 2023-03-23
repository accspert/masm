from django.urls import path
from .views import (
    student_list, create_student, update_student, delete_student,
    teacher_list, create_teacher, update_teacher, delete_teacher)

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/create/', create_student, name='create_student'),
    path('students/<int:pk>/update/', update_student, name='update_student'),
    path('students/<int:pk>/delete/', delete_student, name='delete_student'),

    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/create/', create_teacher, name='create_teacher'),
    path('teachers/<int:pk>/update/', update_teacher, name='update_teacher'),
    path('teachers/<int:pk>/delete/', delete_teacher, name='delete_teacher'),
]
