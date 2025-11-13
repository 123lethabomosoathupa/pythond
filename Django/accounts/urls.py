"""Defines URL patterns for accounts."""

from django.urls import path, include
from . import views

# App namespace to prevent clashes with other apps
app_name = 'accounts'

urlpatterns = [

    # Include all the default authentication URLs provided by Django.
    # This gives you:
    #   /login/    → login page
    #   /logout/   → logout page
    #   /password_change/ and /password_change/done/
    #   /password_reset/ and related reset views
    path('', include('django.contrib.auth.urls')),

    # Custom registration page handled by our own view.
    # /register/ → calls accounts.views.register
    path('register/', views.register, name='register'),
]
