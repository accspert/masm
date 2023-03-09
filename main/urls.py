from django.urls import path

from .views import (
    IndexView, StudentView,
    TeacherView, UpdateRecordView,
    AddRecordView, DeleteRecordView
    )


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('students/', StudentView.as_view(), name='students'),
    path('teachers/', TeacherView.as_view(), name="teachers"),
    path('add/<str:record_type>/', AddRecordView.as_view(), name="add_record"),
    path('<str:record_type>/<int:id>', UpdateRecordView.as_view(),
         name="update_records"),
    path('add/<str:record_type>/<int:id>', DeleteRecordView.as_view(),
         name="delete_record")
]
