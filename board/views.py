from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Post


class IndexView(generic.TemplateView):
    template_name = 'board/index.html'