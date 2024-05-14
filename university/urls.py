from django.urls import path
from django.contrib.auth import views as auth_views

from university import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
