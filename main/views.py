from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView

from .forms import UserRegistrationForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class UserSignupView(SuccessMessageMixin, CreateView):
    template_name = 'signup.html'
    form_class = UserRegistrationForm
    success_url = '/'
    success_message = 'Signup success login to continue'
