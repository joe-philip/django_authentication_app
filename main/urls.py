from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('signup', views.UserSignupView.as_view(), name='signup')
]
