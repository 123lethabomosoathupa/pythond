from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user."""

    # Check the request method.
    # If it's NOT a POST, that means the user is just visiting the page,
    # so we should show them a blank registration form.
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        # If the method IS POST, that means the user submitted the form.
        # Bind the submitted data (request.POST) to a UserCreationForm.
        form = UserCreationForm(data=request.POST)

        # Check if the submitted form is valid (username unique, passwords match, etc.)
        if form.is_valid():
            # Save the new user to the database.
            new_user = form.save()

            # Immediately log the new user in (so they don’t have to log in manually).
            login(request, new_user)

            # Redirect them to the homepage after successful registration.
            return redirect('learning_logs:index')

    # If it's a GET request OR the form is invalid,
    # render the registration page again with the form (blank or with errors).
    context = {'form': form}
    return render(request, 'registration/register.html', context)
