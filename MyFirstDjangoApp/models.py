from django.db import models
from django.contrib.auth.models import User

# Post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.title

# Comment model
class Comment(models.Model):
    content = models.TextField()             
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # Parent comment (optional)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Related post

    def __str__(self):
        return self.content[:20]  # Return the first 20 characters of the comment
