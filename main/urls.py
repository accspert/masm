from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    IndexView, LoginView, LogOutView,
    SignUpView, StudentView,
    TeacherView, UpdateRecordView,
    AddRecordView, DeleteRecordView
    )


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('logout/', login_required(LogOutView.as_view()), name="logout"),
    path('', login_required(IndexView.as_view()), name="index"),
    path('students/', login_required(StudentView.as_view()), name='students'),
    path('teachers/', login_required(TeacherView.as_view()), name="teachers"),
    path('add/<str:record_type>/', login_required(
        AddRecordView.as_view()), name="add_record"),
    path('<str:record_type>/<int:id>', login_required(
        UpdateRecordView.as_view()), name="update_records"),
    path('add/<str:record_type>/<int:id>', login_required(
        DeleteRecordView.as_view()), name="delete_record")
]
