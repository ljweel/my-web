from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)  #hashing
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.comment_text
    