from django.db import models


class GameType(models.Model):
    """
    Model representing a type of game.
    """

    label = models.CharField(max_length=50)
