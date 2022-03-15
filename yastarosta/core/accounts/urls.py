from django.urls import path
from django.conf.urls import include
from yastarosta.core.accounts.views import login_view, registration_view, logout_view

#FixMe подумать над https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Authentication
urlpatterns = [
    path('login/', login_view, name='accounts.login'),
    path('registration/', registration_view, name='accounts.registration'),
    path('logout/', logout_view, name='accounts.logout')
]