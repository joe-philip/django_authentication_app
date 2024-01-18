from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('signup', views.UserSignupView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login')
]
