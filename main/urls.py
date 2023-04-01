from django.urls import path
from .views import (
    student_list, create_student, update_student, DeleteStudent,
    teacher_list, create_teacher, update_teacher, delete_teacher,
    create_course, update_course, delete_course, list_course
)
#from .views import CustomCalendarView, CustomEventJSONView
#from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('students/', student_list, name='student_list'),
    path('students/create/', create_student, name='create_student'),
    path('students/<int:pk>/update/', update_student, name='update_student'),
    path('students/<int:pk>/delete/', DeleteStudent.as_view(), name='delete_student'),

    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/create/', create_teacher, name='create_teacher'),
    path('teachers/<int:pk>/update/', update_teacher, name='update_teacher'),
    path('teachers/<int:pk>/delete/', delete_teacher, name='delete_teacher'),

    path('course/', list_course, name='course_list'),
    path('course/create/', create_course, name='course_create'),
    path('course/<int:pk>/update/', update_course, name='course_update'),
    path('course/<int:pk>/delete/', delete_course.as_view(), name='course_delete'),

    #path('calendar/', login_required(CustomCalendarView.as_view()), name='calendar'),
   # path('calendar_json/', login_required(CustomEventJSONView.as_view()), name='calendar_json'),
]

