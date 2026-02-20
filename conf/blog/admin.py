from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_date','published_date']
    search_fields = ['title', 'category']
    list_filter = ['status', 'published_date']
admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    list_display = ['post', 'is_approved', 'created_date']
admin.site.register(Comment, AdminComment)

admin.site.register(Category)