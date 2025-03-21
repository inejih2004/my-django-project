
from django.contrib.auth.models import User
from django.db import models
class Categorie(models.Model):

    objects = None
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Annonce(models.Model):
    objects = None
    STATUT_CHOICES = [
        ("attente", "attente"),
        ("Acceptée", "Acceptée"),
        ("Rejetée", "Rejetée"),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="annonces")
    image = models.ImageField(upload_to="annonces/", blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default=" en attente")
    date_creation = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

