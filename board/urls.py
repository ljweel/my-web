from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    # ex: /board/
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.postListView.as_view(), name='postList'),
    
]