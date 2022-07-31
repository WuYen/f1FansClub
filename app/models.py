from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=80)
    rank = models.CharField(max_length=100)
    pole = models.CharField(max_length=100)
    champ = models.CharField(max_length=100)
    point = models.CharField(max_length=100)
    icon = models.CharField(max_length=500)
