from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class TheaterName(models.Model):
    TheaterName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Rows = models.IntegerField()
    columns = models.IntegerField()

    def __str__(self):
        return f"{self.TheaterName} - {self.location}"


GENRE_CHOICES = [
    ('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'),
    ('Horror', 'Horror'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'),
    ('Thriller', 'Thriller'), ('Documentary', 'Documentary'),
    ('Animation', 'Animation'), ('Fantasy', 'Fantasy'),
    ('Mystery', 'Mystery'), ('Musical', 'Musical'), ('War', 'War'),
    ('Western', 'Western')
]

class MovieName(models.Model):
    MovieTitle = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default='Action')
    duration = models.TimeField()
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    cast = models.TextField()
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField()
    rating = models.FloatField()

    def __str__(self):
        return self.MovieTitle


SHOW_START_CHOICES = [
    ('10:00 AM', '10:00 AM'),
    ('1:00 PM', '1:00 PM'),
    ('4:00 PM', '4:00 PM'),
    ('7:00 PM', '7:00 PM'),
    ('10:00 PM', '10:00 PM')
]

SHOW_END_CHOICES = [
    ('12:30 PM', '12:30 PM'),
    ('3:30 PM', '3:30 PM'),
    ('6:30 PM', '6:30 PM'),
    ('9:30 PM', '9:30 PM'),
    ('12:30 AM', '12:30 AM')
]

class Showtime(models.Model):
    TheaterNameshow = models.ForeignKey(TheaterName, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    show_start = models.CharField(choices=SHOW_START_CHOICES, max_length=8, null=True, blank=True)
    show_end = models.CharField(choices=SHOW_END_CHOICES, max_length=8, null=True, blank=True)
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.MovieTitle} - {self.show_start} to {self.show_end}"


class Seat(models.Model):
    theater = models.ForeignKey(TheaterName, on_delete=models.CASCADE, related_name='seat')
    row = models.CharField(max_length=5)
    column = models.IntegerField()

    def __str__(self):
        return f"{self.theater.TheaterName} - Row {self.row} Seat {self.column}"


class MovieTicketBooking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
 
    TheaterNameBooked = models.ForeignKey(TheaterName, on_delete=models.CASCADE, null=True)
    seats = models.ManyToManyField(Seat)
    booking_time = models.DateTimeField(auto_now_add=True)
    booked = models.BooleanField(default=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Booking by {self.customer.username} for {self.showtime.movie.MovieTitle} ----{self.showtime.show_start}---{self.showtime.show_end}  at {self.TheaterNameBooked.TheaterName}"


@receiver(post_save, sender=TheaterName)
def create_seats_for_theatre(sender, instance, created, **kwargs):
    """Auto generate seats when a theatre is created"""
    if created and not instance.seat.exists():
        for r in range(instance.Rows):
            row_letter = chr(65 + r)  # Convert row number to ASCII letter
            for c in range(1, instance.columns + 1):
                Seat.objects.create(theater=instance, row=row_letter, column=c)
        print(f"Created {instance.Rows * instance.columns} seats for theater {instance.TheaterName}")