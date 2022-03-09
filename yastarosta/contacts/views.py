from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
class ContactView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
contact_view = ContactView.as_view()