from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth import login


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('posts:index')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_contex_data(**kwargs)
    #     return context
