from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, TemplateView, View

from .forms import LoginForm, UserRegistrationForm
from .models import User


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
            messages.success(self.request, 'Logged in successfully')
            return super().form_valid(form)
        messages.error(
            request=self.request,
            message='Login failed, Invalid credentials'
        )
        return redirect('/login')


class DashboardAPI(View):
    @method_decorator(login_required(login_url='/login'))
    def get(self, request: HttpRequest) -> HttpResponse:
        match request.user.role:
            case 1:
                return render(request, 'dashboard/student.html')
            case 2:
                return render(request, 'dashboard/staff.html')
            case 3:
                context = {'queryset': User.objects.all().exclude(role=3)}
                return render(request, 'dashboard/admin.html', context)
            case 4:
                return render(request, 'dashboard/editor.html')


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('/')
