# events/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, EventForm, BookingForm
from .models import Event, Booking
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.save()
            messages.success(request, "Booking successful!")
            return redirect('dashboard')
    else:
        form = BookingForm()
    return render(request, 'event_detail.html', {'event': event, 'form': form})


@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'bookings': bookings})


@login_required
def manage_events(request):
    if not request.user.is_staff:
        return redirect('home')
    events = Event.objects.all()
    return render(request, 'manage_events.html', {'events': events})


@login_required
def create_event(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_events')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def edit_event(request, event_id):
    if not request.user.is_staff:
        return redirect('home')
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('manage_events')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})


@login_required
def delete_event(request, event_id):
    if not request.user.is_staff:
        return redirect('home')
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('manage_events')
