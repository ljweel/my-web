from django.db import models
from django.conf import settings

class Post(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        verbose_name='작성자', 
        related_name='user_posts'
    )
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    class Meta:
        ordering = ['created_at'] 
        verbose_name = '게시글'
    
    def __str__(self):
        return self.title