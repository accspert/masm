from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *
 
urlpatterns = [
    path('', index,name="home"),
     path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('myadmin/', admin_view, name='myadmin'),
    path('Student/', Student, name='Student'),
    path('CreateStudent/', create_student, name='CreateStudent'),
    path('UpdateStudent/<int:student_id>', update_student, name='UpdateStudent'),
    path('DeleteStudent/<int:student_id>', delete_student, name='DeleteStudent'),


    path('CreateTeacher/', create_Teacher, name='CreateTeacher'),
    path('UpdateTeacher/<int:Teacher_id>', update_Teacher, name='UpdateTeacher'),
    path('DeleteTeacher/<int:Teacher_id>', delete_Teacher, name='DeleteTeacher'),


    path('CreateCourses/', create_Course, name='CreateCourses'),
    path('UpdateCourses/<int:Course_id>', update_Course, name='UpdateCourses'),
    path('DeleteCourses/<int:Course_id>', delete_Courses, name='DeleteCourses'),

    
    path('Courses/', Courses, name='Courses'),
    path('Teacher/', Teacher, name='Teacher'),
    path('logout/', logout_view, name='logout'),
    path('notfound/', custom_404, name='notfound'),
    path('forbidden/', custom_403, name='forbidden'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
