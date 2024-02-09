from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    nom = models.CharField(max_length=60)
    mot_de_passe = models.CharField(max_length=60)