from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Booking

# Signup form using UserCreationForm
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login form
class LoginForm(AuthenticationForm):
    pass  # You can add custom fields or validation here if needed

# Booking form for booking tickets
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event', 'user']  # Adjust fields as necessary
