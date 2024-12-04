from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Voetbalspelers(models.Model):
    naam = models.CharField(max_length=100)
    actuele_club = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Hier kun je extra acties uitvoeren vóór het opslaan
        super().save(*args, **kwargs)

    def __str__(self):
        return self.naam
