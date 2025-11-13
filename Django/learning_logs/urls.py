"""Defines URL patterns for learning_logs."""

# Import the path() function to define URL routes
from django.urls import path

# Import views so we can map URLs to view functions
from . import views

# Set an application namespace.
# This helps distinguish these URLs from those of other apps in the project.
app_name = 'learning_logs'

# A list of URL patterns for this app.
urlpatterns = [

    # Home page → calls the index view
    path('', views.index, name='index'),

    # Page that shows all topics → calls the topics view
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    # <int:topic_id> captures a number from the URL and passes it to the view.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic → calls the new_topic view
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry under a specific topic.
    # <int:topic_id> tells Django which topic this entry belongs to.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an existing entry.
    # <int:entry_id> captures the ID of the entry to be edited.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
