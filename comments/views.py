# comments/views.py

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from .models import Comment
from .forms import CommentForm
from posts.models import Post

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        post_pk = self.kwargs.get('pk') 
        post = get_object_or_404(Post, pk=post_pk)
        
        form.instance.author = self.request.user
        form.instance.post = post
        form.instance.parent = None
        return super().form_valid(form)
    
    def get_success_url(self):
        post_pk = self.kwargs.get('pk')
        return reverse('posts:detail', kwargs={'pk': post_pk})
