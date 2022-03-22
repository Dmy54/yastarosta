from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class StudentGroupView(LoginRequiredMixin, TemplateView):
    template_name = 'student_group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
contact_view = StudentGroupView.as_view()