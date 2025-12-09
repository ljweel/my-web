from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    # ex: /board/
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.postListView.as_view(), name='list'),
    path('post/<int:pk>/', views.postDetailView.as_view(), name='detail'),
    path('post/create/', views.postCreateView.as_view(), name='create'),
    path('about/', views.AboutView.as_view(), name='about'),
]