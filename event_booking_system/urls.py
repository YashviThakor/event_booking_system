# urls.py
from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('event/<int:pk>/', views.event_detail_view, name='event_detail'),
    path('event/<int:pk>/book/', views.book_ticket_view, name='book_ticket'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
