from django.db import models
from django.db.models import 
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Event(models.Model):
    """Class for top level Events, that contain one or multiple Tournaments."""

    name = models.CharField(max_length=50, help_text="Name of Event")
    description = models.CharField(max_length=250, help_text="Short description of Event")
    
    # One to Many relationship to Tournaments class
    #tournaments = models.ForeignKey()

    class Meta:
        ordering = [
            "name",
            "pk",
            "description",
        ]
    
    # Methods
    def __str__(self):
        """String for representing Event object."""
        return self.name

class Tournament(models.Model):
    """Class for Tournaments, that contain one or many brackets."""

    name = models.CharField(max_length=50, help_text="Name of Tournament")

    class Meta:
        ordering = [
            "name",
            "pk",
        ]
    
    def __str__(self):
        """String representation."""
        return self.name