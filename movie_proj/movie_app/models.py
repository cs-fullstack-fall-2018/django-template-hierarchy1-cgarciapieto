from django.db import models

# Create your models here.
class Blockbuster(models.Model):
    name = models.CharField(max_length=100)
    yearReleased = models.IntegerField()
    ageAllowed = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name