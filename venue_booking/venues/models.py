from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Venue(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(default=0)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    address = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='venues/', null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('venue', 'user')

    def __str__(self):
        return f"{self.user.username}'s review for {self.venue.name}"

class Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')

    def __str__(self):
        return f"Booking for {self.venue.name} by {self.user.username}"