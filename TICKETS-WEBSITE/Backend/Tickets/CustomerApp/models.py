from django.db import models

from django.contrib.auth.models import User

genre=[('Action','Action'),
       ('Comedy','Comedy'),
       ('Drama','Drama'),
       ('Horror','Horror'),
       ('Romance','Romance'),
       ('Sci-Fi','Sci-Fi'),
       ('Thriller','Thriller'),
       ('Documentary','Documentary'),
       ('Animation','Animation'),
       ('Fantasy','Fantasy'),
       ('Mystery','Mystery'),
       ('Musical','Musical'),
       ('War','War'),
       ('Western','Western')]
class MovieName(models.Model):
    MovieTitle = models.CharField(max_length=100)

    genre = models.CharField(max_length=100, choices=genre, default='Action')
    duration = models.CharField(max_length=100)

    release_date = models.DateField()
    director = models.CharField(max_length=100)
    cast = models.TextField()
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField()
    rating = models.FloatField()


    def __str__(self):
        return self.MovieTitle
    
class Showtime(models.Model):
    movie = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    show_date = models.DateField()
    show_time = models.TimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.MovieTitle} - {self.show_date} {self.show_time}"
class TheaterName(models.Model):
    TheaterName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Rows = models.IntegerField()
    SeatsPerRow = models.IntegerField()
    columns = models.IntegerField()
class Seat(models.Model):
    theater = models.ForeignKey(TheaterName, on_delete=models.CASCADE)
    row = models.CharField(max_length=5)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.theater.TheaterName} - Row {self.row} Seat {self.number}"    

class Tickets(models.Model):    
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.showtime.movie.MovieTitle} - Seat {self.seat_number}"

class MovieTicketBooking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Tickets)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.customer.username} for {self.showtime.movie.MovieTitle}"