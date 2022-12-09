from django.db import models

from django.contrib.auth.models import AbstractUser
from num2words import num2words


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
    client=models.ForeignKey(Client, on_delete=models.CASCADE,related_name="voir_staff")
    date=models.DateField(auto_now_add=True)
    designation=models.CharField(max_length=200)
    poids_en_grammes=models.IntegerField()
    titre_en_caract=models.IntegerField()
    prix_unitaire=models.IntegerField(default=40)
    def line_total(self):
         return self.poids_en_grammes * self.prix_unitaire
    def numwords(self):
        line_num=self.poids_en_grammes * self.prix_unitaire
        return num2words(line_num, lang='fr')
        

    # prix_total=models.IntegerField()

# class Attestation(models.Model):
#     facture=models.ForeignKey(Facture, on_delete=models.CASCADE)
#     client=models.ForeignKey(Client, on_delete=models.CASCADE)
    
class BordereauAdministratif(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE,related_name="voir")
    parametre=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    numero_ordre=models.IntegerField()
    type_echantillon=models.CharField(max_length=500)












    
