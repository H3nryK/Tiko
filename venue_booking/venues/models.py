from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='venues', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='venues', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, related_name='bookings', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.venue} on {self.date}"
