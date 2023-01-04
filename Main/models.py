from io import BytesIO
from django.db import models

from django.contrib.auth.models import AbstractUser
from num2words import num2words
import qrcode
# from barcode.writer import ImageWriter
from django.core.files import File
from PIL import Image, ImageDraw



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
    telephone=models.CharField(max_length=200,unique=True)
    email=models.CharField(max_length=200,unique=True)
    sexe=models.CharField(max_length=200)


class Facture(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE,related_name="voir_staff")
    date=models.DateField(auto_now_add=True)
    designation=models.CharField(max_length=200)
    poids_en_grammes=models.IntegerField()
    titre_en_caract=models.IntegerField()
    # user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='qr_codes', blank=True)
    prix_unitaire=models.IntegerField(default=40)
    # barre0=models.CharField(max_length=1,null=True)
    # barre1=models.CharField(max_length=6,null=True)
    # barre2=models.CharField(max_length=5,null=True)

    def save(self,*args, **kwargs):
        qrcode_image=qrcode.make(self.designation)
        canvas=Image.new('RGB',(290,290),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image)
        fname=f'image-{self.designation}'+'.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.image.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
    #     ean=EAN(f'{self.barre0}{self.barre1}{self.barre2}', writer=ImageWriter(format='PNG'))
    #     buffer=BytesIO()
    #     ean.writer(buffer)
    #     self.barcode.save("pngtree-barcode-vector-png-image_4889246.PNG", File(buffer), save=False)
    #     return super().save(*args, **kwargs)

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
    # admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    parametre=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    numero_ordre=models.IntegerField()
    type_echantillon=models.CharField(max_length=500)













    
