from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('signup', views.UserSignupView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.DashboardAPI.as_view(), name='dashboard')
]
