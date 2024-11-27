from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserListAPIView, UserCreateAPIView 

urlpatterns = [
    path('', UserListAPIView.as_view(), name="api users list"),
    path('register/', UserCreateAPIView.as_view(), name="api users register"),

    # jwt
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	
]
