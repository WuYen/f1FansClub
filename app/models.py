from django.db import models

# Create your models here.


class Team():
    def __init__(self, name, rank) -> None:
        self.name = name
        self.rank = rank
        self.pole = ''
        self.champ = ''
        self.point = ''
        self.icon = ''
        self.drivers = ''
