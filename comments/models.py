# comments/models.py

from django.db import models
from django.conf import settings
from posts.models import Post 

class Comment(models.Model):
    # 1. 게시글 관계: 어떤 게시글에 달린 댓글인지 명확히 지정
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name='게시글'
    )
    
    # 2. 작성자 관계 (인증 필수): JWT 인증을 통해 획득한 User 모델과 연결
    # settings.AUTH_USER_MODEL을 사용하여 Django의 기본 또는 커스텀 User 모델을 참조
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='user_comments',
        verbose_name='작성자'
    )
    
    # 3. 댓글 내용
    comment_text = models.TextField(verbose_name='내용')
    
    # 4. 계층 구조 (대댓글) 구현의 핵심!
    # 자기 자신(Comment)을 참조하며, 최상위 댓글은 null=True
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, # 부모 댓글이 삭제되어도 자식 댓글은 남김
        null=True, 
        blank=True,
        related_name='replies', # 자식 댓글을 조회할 때 사용할 이름
        verbose_name='부모 댓글'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    class Meta:
        ordering = ['created_at'] 
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'
        
    def __str__(self):
        return f'{self.author.username}의 댓글: {self.comment_text[:15]}...'