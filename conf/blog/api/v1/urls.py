from rest_framework import routers
from . import views

app_name = 'api'


router = routers.DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
router.register('comment', views.CommentViewSet, basename='comment')
urlpatterns = router.urls