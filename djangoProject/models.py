from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


CHOICES = [
    ("SG","single"),
    ("MA","married"),
    ("WI", "widow")
]

class Game(models.Model):

    name = models.CharField(max_length=15, blank=False, primary_key=True)
    developer = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.name

class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    administrator = models.BooleanField(blank=False, default=False)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(100),
            MinValueValidator(18)])
    password = models.CharField(max_length=8)
    civil_state = models.CharField(choices=CHOICES, max_length=10)
    games = models.ManyToManyField(Game, blank=False)


    def __str__(self):
        return self.name

