# events/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the User model
from .models import Event, Booking


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Now User is correctly imported and can be used
        fields = ['username', 'email', 'password1', 'password2']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image', 'price']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_tickets']
