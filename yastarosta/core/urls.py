from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('accounts/', include('yastarosta.core.accounts.urls'))
]