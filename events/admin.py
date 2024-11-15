from django.contrib import admin
from .models import Event, Booking

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description', 'total_bookings')
    search_fields = ('name',)
    list_filter = ('date',)

    def total_bookings(self, obj):
        return obj.booking_set.count()
    total_bookings.short_description = 'Total Bookings'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'date_booked')
    search_fields = ('user__username', 'event__name')
