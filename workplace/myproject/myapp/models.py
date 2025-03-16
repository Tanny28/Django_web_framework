from django.db import models
from django.utils import timezone  # Import timezone

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name 
class Booking(models.Model):
    
   
    date = models.DateTimeField(default=timezone.now)  # Add a default value


    def __str__(self):
        return self.name