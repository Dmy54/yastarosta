from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login
from yastarosta.core.accounts.forms import LoginForm

# Create your views here.
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
        else:
            return HttpResponse('no such user')
        return render(self.request, self.template_name)
login_view = LoginView.as_view()