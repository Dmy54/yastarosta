from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
class LoginView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
login_view = LoginView.as_view()