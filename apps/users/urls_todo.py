from .views import TodoListAPIView
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("api_todo", TodoListAPIView, basename='api-todo')

urlpatterns = [

]

urlpatterns += router.urls