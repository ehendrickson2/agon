"""Tournament Bracket data models."""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Class for Custom User model."""


class Event(models.Model):
    """Class for top level Events, that contain one or multiple Tournaments."""

    name = models.CharField(max_length=50, help_text="Name of Event")
    short_description = models.CharField(
        max_length=250, help_text="Short description of Event"
    )
    description = models.TextField()
    url = models.URLField()
    venue = models.CharField(max_length=50, help_text="Venue name or Address")

    class Meta:
        """Meta for Event class."""

        ordering = [
            "pk",
            "name",
            "short_description",
            "description",
            "url",
            "venue",
        ]

    # Methods
    def __str__(self):
        """String for representing Event object."""
        return f"{self.name}"


class Tournament(models.Model):
    """Class for tournament object."""

    name = models.CharField(max_length=50, help_text="Name of Tournament")
    description = models.TextField()
    url = models.URLField()
    host = models.CharField(max_length=50, help_text="Host of this tournament bracket")
    # Many to Many to game class
    # game = models.ManyToManyField(Games)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        """Meta for Tournament class."""

        ordering = [
            "pk",
            "name",
        ]

    def __str__(self):
        """String representation."""
        return f"{self.name}"
