from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone


from .forms import PostForm
from .models import Post

class IndexView(generic.TemplateView):
    template_name = 'posts/index.html'


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


class postCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/postCreateForm.html'
    success_url = reverse_lazy('post:list')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class AboutView(generic.TemplateView):
    template_name = 'about.html'