"""Tournament Bracket data models."""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    """Class for Custom User model."""


class Game(models.Model):
    """Class for Game choice set."""

    name = models.CharField(
        max_length=50,
        help_text="Name of game title",
    )


class BracketType(models.Model):
    """Class for Bracket Types."""

    name = models.CharField(
        max_length=50,
    )


class Event(models.Model):
    """Class for top level Events, that contain one or multiple Tournaments."""

    name = models.CharField(
        max_length=50,
        help_text="Name of Event",
    )
    short_description = models.CharField(
        max_length=250,
        help_text="Short description of Event",
    )
    description = models.TextField()
    url = models.URLField()
    venue = models.CharField(
        max_length=50,
        help_text="Venue name or Address",
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    timezone = models.CharField(
        max_length=50,
        help_text="Timezone for this event",
    )

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
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    host = models.CharField(
        max_length=50,
        help_text="Host of this tournament bracket",
    )
    game = models.ManyToManyField(
        to=Game,
        related_name="tournament",
        verbose_name="Game(s)",
    )
    bracket_format = models.ManyToManyField(
        to=BracketType,
        related_name="tournament",
        verbose_name="Bracket format(s)",
    )
    participants = models.PositiveIntegerField(
        help_text="Maximum number of participants",
    )
    start_time = models.DateTimeField()

    class Meta:
        """Meta for Tournament class."""

        ordering = [
            "pk",
            "name",
            "description",
            "host",
            "url",
            "event",
            "game",
            "bracket_format",
            "participants",
            "start_time",
        ]

    def __str__(self):
        """String representation."""
        return f"{self.name}"
