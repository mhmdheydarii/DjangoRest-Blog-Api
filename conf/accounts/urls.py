from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('api/v1/', include('api.v1.urls'))
]