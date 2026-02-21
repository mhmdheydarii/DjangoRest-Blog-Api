from rest_framework import serializers
from blog.models import Post, Comment, Category

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')

    class Meta:
        model = Post
        fields = ['id','title', 'content', 'snippet', 'category', 'status', 'absolute_url', 'published_date']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    
    
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        return rep

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'title', 'message', 'is_approved', 'created_date']
        read_only_fields = ['is_approved']