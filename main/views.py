from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView, TemplateView

from .forms import LoginForm, UserRegistrationForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class UserSignupView(SuccessMessageMixin, CreateView):
    template_name = 'signup.html'
    form_class = UserRegistrationForm
    success_url = '/login'
    success_message = 'Signup success login to continue'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form: LoginForm) -> HttpResponse:
        if user := authenticate(self.request, **form.cleaned_data):
            login(self.request, user=user)
            return super().form_valid(form)
        messages.error(
            request=self.request,
            message='Login failed, Invalid credentials'
        )
        return redirect('/login')
