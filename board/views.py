from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post

class IndexView(generic.TemplateView):
    template_name = 'board/index.html'


class postListView(generic.ListView):
    template_name = 'board/postList.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]