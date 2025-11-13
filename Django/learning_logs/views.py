from django.shortcuts import render, redirect             # Helpers to render templates and redirect to a URL
from django.contrib.auth.decorators import login_required # Decorator that forces the user to be logged in
from django.http import Http404                           # Exception that returns a 404 Not Found response

from .models import Topic, Entry                          # Your app's data models
from .forms import TopicForm, EntryForm                   # ModelForm classes for creating/editing Topic and Entry


def index(request):                                       # View function for the home page; takes the HTTP request
    """The home page for Learning Log."""                 # Docstring describing the view
    return render(request, 'learning_logs/index.html')    # Render and return the template with an empty context


@login_required                                           # Require authentication before accessing this view
def topics(request):                                      # View that lists all topics for the logged-in user
    """Show all topics belonging to the logged-in user."""# Docstring explaining purpose
    topics = Topic.objects.filter(                        # Build a queryset of Topic rows...
        owner=request.user                                # ...limited to the current user only
    ).order_by('date_added')                              # ...ordered oldest → newest by creation time
    context = {'topics': topics}                          # Context dictionary passed to the template
    return render(request, 'learning_logs/topics.html',   # Render the list template...
                  context)                                # ...with the topics in context


@login_required                                           # Only logged-in users can see a specific topic
def topic(request, topic_id):                             # View that shows one topic plus all its entries
    """Show a single topic and all its entries."""        # Docstring
    topic = Topic.objects.get(id=topic_id)                # Fetch the Topic by primary key (may raise DoesNotExist)

    # NOTE: your original code had "raise Htt" here — that will crash.
    # It must be Http404 to correctly return a 404 response.

    if topic.owner != request.user:                       # Authorization check: topic must belong to current user
        raise Http404                                     # If not, pretend it doesn't exist (security best practice)

    entries = topic.entry_set.order_by('-date_added')     # Reverse-chronological list of related Entry objects
    context = {'topic': topic, 'entries': entries}        # Provide both topic and entries to the template
    return render(request, 'learning_logs/topic.html',    # Render the detail page...
                  context)                                # ...with the context


@login_required                                           # Only logged-in users can create topics
def new_topic(request):                                   # View for creating a new Topic
    """Add a new topic."""                                # Docstring
    if request.method != 'POST':                          # If the request is GET (or anything not POST)...
        form = TopicForm()                                # ...show an empty form to the user
    else:                                                 # Otherwise it's a POST with submitted data
        form = TopicForm(data=request.POST)               # Bind POST data to the form
        if form.is_valid():                               # Server-side validation passes?
            new_topic = form.save(commit=False)           # Create Topic instance but don't save to DB yet
            new_topic.owner = request.user                # Attach the current user as the owner
            new_topic.save()                              # Now save to the database
            return redirect('learning_logs:topics')       # Redirect to the topics list after success

    context = {'form': form}                              # If GET or invalid form, re-render the page with the form
    return render(request, 'learning_logs/new_topic.html',
                  context)


@login_required                                           # Only logged-in users can add entries
def new_entry(request, topic_id):                         # View for creating an Entry under a specific Topic
    """Add a new entry for a particular topic."""         # Docstring
    topic = Topic.objects.get(id=topic_id)                # Fetch the parent Topic (may raise DoesNotExist)
    if topic.owner != request.user:                       # Authorization: ensure user owns this topic
        raise Http404                                     # If not, hide existence

    if request.method != 'POST':                          # If this is a GET request...
        form = EntryForm()                                # ...show an empty Entry form
    else:                                                 # Otherwise, process POSTed data
        form = EntryForm(data=request.POST)               # Bind POST data to the form
        if form.is_valid():                               # Validate
            new_entry = form.save(commit=False)           # Create Entry instance without committing yet
            new_entry.topic = topic                       # Link the entry to its Topic
            new_entry.save()                              # Save to the database
            return redirect('learning_logs:topic',        # Redirect to the topic detail page...
                            topic_id=topic_id)            # ...so the user can see their new entry

    context = {'topic': topic, 'form': form}              # Provide topic (for heading) and form to the template
    return render(request, 'learning_logs/new_entry.html',
                  context)


@login_required                                           # Only logged-in users can edit entries
def edit_entry(request, entry_id):                        # View for editing an existing Entry
    """Edit an existing entry."""                         # Docstring
    entry = Entry.objects.get(id=entry_id)                # Fetch the Entry to edit (may raise DoesNotExist)
    topic = entry.topic                                   # Convenience: the Entry's parent Topic

    # (Recommended) Security check could go here:
    # if topic.owner != request.user: raise Http404

    if request.method != 'POST':                          # For GET requests...
        form = EntryForm(instance=entry)                  # ...pre-fill the form with the current entry data
    else:                                                 # For POST requests...
        form = EntryForm(instance=entry, data=request.POST)# ...bind POST data to the form for the same instance
        if form.is_valid():                               # Validate input
            form.save()                                   # Save changes to the Entry
            return redirect('learning_logs:topic',        # Redirect back to the topic detail page
                            topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}# Provide everything the template needs
    return render(request, 'learning_logs/edit_entry.html',
                  context)
