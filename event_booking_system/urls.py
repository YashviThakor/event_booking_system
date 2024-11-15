# event_booking_system/urls.py

from django.contrib import admin
from django.urls import path, include
from events import views  # Make sure to import views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name='signup'),  # Update the view name to sign_up
    path('', views.login_view, name='login'),  # Make sure login_view is defined
    path('home/', views.home, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage_events/', views.manage_events, name='manage_events'),
    path('create_event/', views.create_event, name='create_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    
    # Add Django's built-in auth URLs for login/logout
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login/logout URLs
]
