from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView)
from . import views

app_name = 'api'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view()),
]