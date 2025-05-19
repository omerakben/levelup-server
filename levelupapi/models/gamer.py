from django.db import models


class Gamer(models.Model):
    """
    Model representing a gamer.
    """

    uid = models.IntegerField()
    bio = models.CharField(max_length=100)
