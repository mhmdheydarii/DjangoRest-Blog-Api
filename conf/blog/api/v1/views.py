from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from blog.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .paginations import CustomPostPagination, CustomCommentPagination


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['category', 'published_date']
    pagination_class = CustomPostPagination
        

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = CustomCommentPagination
