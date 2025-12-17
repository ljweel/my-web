from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.utils import timezone


from .forms import PostForm
from .models import Post
from comments.forms import CommentForm
from comments.models import Comment

class postListView(generic.ListView):
    template_name = 'posts/postList.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.filter(
            created_at__lte=timezone.now()
        ).order_by('-created_at')[:5]
    
class postDetailView(generic.DeleteView):
    model = Post
    template_name = 'posts/postDetail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

        context['comments'] = Comment.objects.filter(
            post = self.get_object(),
            parent__isnull=True,
        ).order_by('created_at')

        return context

class postCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/postCreateForm.html'
    success_url = reverse_lazy('posts:list')

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class AboutView(generic.TemplateView):
    template_name = 'about.html'