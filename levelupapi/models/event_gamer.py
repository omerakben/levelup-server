from django.db import models

from .event import Event
from .gamer import Gamer


class EventGamer(models.Model):
    """Model representing a relationship between a gamer and an event."""

    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
