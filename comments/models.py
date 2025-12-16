# comments/models.py

from django.db import models
from django.conf import settings
from posts.models import Post 

class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name='게시글'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='user_comments',
        verbose_name='작성자'
    )
    # 자기 자신(Comment)을 참조
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='replies', # 자식 댓글을 조회할 때 사용할 이름
        verbose_name='부모 댓글'
    )
    comment_text = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    class Meta:
        ordering = ['created_at'] 
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록' # 복수
        
    def __str__(self):
        return f'{self.author.username}의 댓글: {self.comment_text[:15]}...'