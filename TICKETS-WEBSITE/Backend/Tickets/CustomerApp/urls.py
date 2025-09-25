from django.urls import path
from .views import *

urlpatterns = [
    #path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    #path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
   # path('register/', RegisterUserView.as_view(), name='register'),
  path("moviename/",MovieNameView.as_view(),name="movieName"),
   path("showtime/",ShowTimeView.as_view(),name="Showtime"),
    path("Theatrename/",TheatreNameView.as_view(),name="Theatre"),
     path("seat/",SeatView.as_view(),name="Seat"),
      path("Movieticketing/",MovieTicketingView.as_view(),name="Ticketing"),

    

]
