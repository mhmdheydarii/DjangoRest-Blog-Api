from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    # author =
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="Posts/" ,null=True, blank=True)
    # like =
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.content[:90]

    
    class Meta:
        ordering = ['-published_date']



class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    # user = 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    title = models.CharField(max_length=250)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_date']
