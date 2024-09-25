from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom= models.CharField(max_length=100)
    prenom= models.CharField(max_length=100)
    matricule=models.CharField(max_length=20, unique=True)
    telephone= models.CharField(max_length=15)
    address= models.TextField()
    filiere=models.CharField(max_length=100)
    niveau_etudes=models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__() + self.nom + self.prenom
