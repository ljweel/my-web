# comments/forms.py

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_text'].widget.attrs.update({
            'placeholder': '댓글을 입력하세요...',
            'rows': 3,
            'class': 'form-control comment-input'
        })

    class Meta:
        model = Comment
        fields = ['comment_text']