
from django.contrib import admin
from django.urls import path

from mysite.api.views import login_view, register_view

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('register/', register_view, name = "register"),
]
