from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SignupForm, LoginForm, BookingForm
from .models import Event, Booking
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Custom form handling
            login(request, user)  # Log the user in
            next_url = request.GET.get('next', 'home')  # Get the next URL or default to 'home'
            return redirect(next_url)  # Redirect to the next page or home
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
# Home page view (requires login)
@login_required
def home_view(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

# Event detail view (requires login)
@login_required
def event_detail_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

# Book ticket view (requires login)
@login_required
def book_ticket_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.save()
            return redirect('dashboard')  # Redirect to dashboard after booking
    else:
        form = BookingForm()
    return render(request, 'book_ticket.html', {'form': form, 'event': event})

# Dashboard view (requires login)
@login_required
def dashboard_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'bookings': bookings})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logging out
