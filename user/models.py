from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    description = models.TextField(blank=True)
    count = models.IntegerField()
    status_choices = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')
    
    def __str__(self):
        return f"{self.event_name} event booked by {self.name}"
    
