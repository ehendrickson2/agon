"""Tournament Bracket data models."""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from choices import STATUS_CHOICES


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
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="upcoming")
    rules = models.TextField(
        blank=True, help_text="Custom rules or notes for participants."
    )
    url = models.URLField()
    logo = models.ImageField(upload_to="tournament_logos/", null=True, blank=True)
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
    max_participants = models.PositiveIntegerField(
        help_text="Maximum number of participants",
        default=32,
    )
    start_time = models.DateTimeField()
    registration_open = models.DateTimeField(null=True, blank=True)
    registration_close = models.DateTimeField(null=True, blank=True)
    is_public = models.BooleanField(default=True)

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


class Participant(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    is_team = models.BooleanField(default=False)
    seed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Round(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=50)  # e.g. "Quarterfinals"

    def __str__(self):
        return f"{self.name} - Round {self.number}"


class Match(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name="matches")
    match_number = models.IntegerField()
    player1 = models.ForeignKey(
        Participant,
        on_delete=models.SET_NULL,
        null=True,
        related_name="player1_matches",
    )
    player2 = models.ForeignKey(
        Participant,
        on_delete=models.SET_NULL,
        null=True,
        related_name="player2_matches",
    )
    winner = models.ForeignKey(
        Participant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="won_matches",
    )
    scheduled_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.tournament.name} - Match {self.match_number}"
