from django.shortcuts import render
from studApp.serializer import StudentSerializer,UserSerializer
from studApp.models import StudentModel
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.filters import SearchFilter

# Create your views here.

class UserCreate(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class StudentCreate(ListCreateAPIView):
    serializer_class=StudentSerializer
    queryset=StudentModel.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    filter_backends=[SearchFilter]
    search_fields=['name','course']

    def get_queryset(self):
        return StudentModel.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return StudentModel.objects.filter(owner=self.request.user)
