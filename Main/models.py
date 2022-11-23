from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type_data=((1,"ADMIN"), (2,"STAFF"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=20)

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Client(models.Model):
    nom= models.CharField(max_length=200)
    prenom= models.CharField(max_length=200)
    adresse= models.CharField(max_length=200)
    telephone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    sexe=models.CharField(max_length=200)


class Facture(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    designation=models.CharField(max_length=200, default="lingots d'or")
    poids_en_grammes=models.IntegerField()
    titre_en_caract=models.IntegerField()
    prix_unitaire=models.IntegerField(default=40)
    prix_total=models.IntegerField()

class Attestation(models.Model):
    facture=models.ForeignKey(Facture, on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    













    
