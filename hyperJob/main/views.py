from django.shortcuts import render
from django.views import View

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView


class MainMenu(View):
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = '../login/'
    template_name = 'singup.html'


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    redirect_field_name = '/'


