# accounts/urls.py

from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import*

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    # 비밀번호 변경/재설정 뷰도 필요시 추가
]