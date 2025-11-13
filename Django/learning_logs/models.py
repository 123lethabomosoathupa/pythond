from django.db import models
from django.contrib.auth.models import User  # Built-in Django user model for authentication


class Topic(models.Model):
    """A topic the user is learning about."""

    # A short piece of text (max 200 chars) describing the topic
    text = models.CharField(max_length=200)

    # Stores the date/time when the topic is created (set automatically once)
    date_added = models.DateTimeField(auto_now_add=True)

    # Link each topic to a user (the owner).
    # CASCADE means: if the user is deleted, delete their topics too.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model (the topic text)."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    # Each entry is linked to a specific topic.
    # CASCADE: if a topic is deleted, delete its entries too.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # The actual text of the entry (no length limit).
    text = models.TextField()

    # Timestamp for when the entry was created (set automatically once).
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Changes the plural name in the admin site from "Entrys" to "Entries".
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry (first 50 characters)."""
        return f"{self.text[:50]}..."
