from django.db import models


class Gamer(models.Model):
    """
    Model representing a gamer.
    """

    uid = models.CharField(
        max_length=255
    )  # Changed to CharField to store Firebase string UIDs
    bio = models.CharField(
        max_length=500
    )  # Increased max_length for bio as well, just in case
