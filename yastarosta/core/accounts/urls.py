from django.urls import path
from django.conf.urls import include
from yastarosta.core.accounts.views import login_view

urlpatterns = [
    path('login/', login_view, name='accounts.login')
]