from django.urls import path
from .views import StudentList, StudentDetail

urlpatterns = [
    path("", StudentList.as_view(), name="student_list"),
    path("<int:pk>/", StudentDetail.as_view(), name="student_detail"),
]
