from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView)
from . import views

app_name = 'api'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify')
]