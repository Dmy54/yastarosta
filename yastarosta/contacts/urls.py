from django.urls import path
from yastarosta.contacts.views import contact_view


urlpatterns = [
    path('contacts/', contact_view, name='contacts.list')
]