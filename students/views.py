from django.db.models import query
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .permissions import IsOwnerOrReadOnly
from .serializers import StudentSerializer

# Create your views here.


class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
