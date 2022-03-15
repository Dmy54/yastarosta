from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.base import RedirectView, TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from yastarosta.core.accounts.forms import (
    LoginForm,
    RegistrationForm
)


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = LoginForm()
        context['login_form'] = form
        return context

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('contacts.list'))
        else:
            return redirect(reverse('accounts.login'))
login_view = LoginView.as_view()


class RegistrationView(TemplateView):
    template_name = 'registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RegistrationForm()
        context['registration_form'] = form
        return context

    def post(self, request):
        # FixME применить pydantic
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create(username, email, password)
        user.name = name
        user.save()
registration_view = RegistrationView.as_view()


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('accounts.login'))
logout_view = LogoutView.as_view()
