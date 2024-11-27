from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import mixins
from .models import User, Todo
from .serializers import UserSerializer, UserRegisterSerializer, TodoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
# Create your views here.
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class TodoListAPIView(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = Pagination