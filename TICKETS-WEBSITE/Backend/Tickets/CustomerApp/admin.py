from django.contrib import admin
from .models import MovieName,MovieTicketBooking,Showtime,TheaterName,Seat,Tickets,Booking
# Register your models here.
admin.site.register(MovieName)
admin.site.register(TheaterName)
admin.site.register(Showtime)
admin.site.register(Seat)
admin.site.register(Tickets)
admin.site.register(MovieTicketBooking)

