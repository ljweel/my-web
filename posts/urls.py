from django.urls import path

from . import views
from comments.views import CommentCreateView
app_name = 'posts'
urlpatterns = [
    path('', views.postListView.as_view(), name='list'),
    path('<int:pk>/', views.postDetailView.as_view(), name='detail'),
    path('create/', views.postCreateView.as_view(), name='create'),
    # 댓글 생성 뷰 (폼 제출 타겟)
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),

]   