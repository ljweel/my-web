from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.postListView.as_view(), name='list'),
    path('<int:pk>/', views.postDetailView.as_view(), name='detail'),
    path('create/', views.postCreateView.as_view(), name='create'),
]   