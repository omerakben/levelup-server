from django.db import models

from .game_type import GameType
from .gamer import Gamer


class Game(models.Model):
    """
    Model representing a game.
    """

    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
