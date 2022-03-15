from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from yastarosta.contacts.models import Contact


class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = Contact.objects.all()
        context['contacts'] = contacts
        return context
contact_view = ContactView.as_view()