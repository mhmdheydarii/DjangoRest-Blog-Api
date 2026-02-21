from django.urls import path, include
from .views import *

urlpatterns = [
    path('hello/', hello),
    path('api/v1/', include('blog.api.v1.urls'))
]