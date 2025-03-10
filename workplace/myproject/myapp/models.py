from django.db import models
from django.utils import timezone  # Import timezone

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name
class Booking(models.Model):
    
   
    date = models.DateTimeField(default=timezone.now)  # Add a default value


    def __str__(self):
        return self.name