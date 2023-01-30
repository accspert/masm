from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index,login_view,signup_view,admin_view,logout_view,custom_403,custom_404,Student,Courses

 
urlpatterns = [
    path('', index,name="home"),
     path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('myadmin/', admin_view, name='myadmin'),
    path('Student/', Student, name='Student'),
    path('Courses/', Courses, name='Courses'),
    path('logout/', logout_view, name='logout'),
    path('notfound/', custom_404, name='notfound'),
    path('forbidden/', custom_403, name='forbidden'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
