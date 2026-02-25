from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView)
from . import views

app_name = 'api'

urlpatterns = [
    # reistration 
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    # create access and refresh token
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
    # get new access from refresh token
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    # check token
    path('verify/', TokenVerifyView.as_view(), name='verify')
]