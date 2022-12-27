from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,get_object_or_404

from Main.EmailBackend import EmailBackend
from Main.models import Client
from .models import *



# Create your views here.


# @login_required(login_url="/")
def index(request):
    clients=Client.objects.all()
    return render(request, 'administrateur/index.html',{"clients":clients})

def index_staff(request):
    clients=Client.objects.all()
    return render(request, 'staff/index_staff.html',{"clients":clients})

def acceuil(request):
    total_client = Client.objects.all().count()
    total_facture = Facture.objects.all().count()
    context = {
        
        'total_client': total_client,
        'total_facture': total_facture
        
    }
    return render(request, 'administrateur/acceuil.html',context)



def liste_facture(request):
    facts=Facture.objects.all()
    return render(request, 'administrateur/liste_facture.html',{"facts":facts})



def login(request):
    return render(request, 'administrateur/login.html')


# @login_required(login_url="/")
def voir(request,client_id):
    affiche_facture=Client.objects.get(id=client_id)
    return render(request, 'administrateur/voir_admin.html',{'voir_staff':affiche_facture})



def voir_facture(request,client_id,facture_id):
    affiche_cli=Client.objects.get(id=client_id)
    affiche_facture=Facture.objects.get(id=facture_id)
    # numwords=num2words(line_total, lang='fr')
    context = {
        
        'voir_staff': affiche_facture,
        'voir_staff': affiche_cli
        
    }
    return render(request, 'staff/facture.html',context)

def ba(request,client_id,ba_id):
    affiche_cli=Client.objects.get(id=client_id)
    affiche_ba=BordereauAdministratif.objects.get(id=ba_id)
    # numwords=num2words(line_total, lang='fr')
    context = {
        'voir': affiche_ba,
        'voir': affiche_cli
    }
    return render(request, 'staff/ba.html',context)


def voir_attestation(request,client_id,facture_id):
    affiche_cli=Client.objects.get(id=client_id)
    affiche_attest=Facture.objects.get(id=facture_id)
    # numwords=num2words(line_total, lang='fr')
    context = {
        'voir_staff': affiche_attest,
        'voir_staff': affiche_cli
    }
    return render(request, 'administrateur/attestation.html',context)


def voir_staff(request,client_id):
    affiche_facture=Client.objects.get(id=client_id)
    return render(request, 'staff/voir.html',{'voir_staff':affiche_facture})

def voir_ba(request, client_id):
    affiche_ba=Client.objects.get(id=client_id)
    return render(request, "staff/voir_ba.html",{'voir':affiche_ba})

def ajouter_facture(request,client_id):
    affiche_client=Client.objects.get(id=client_id)

    if request.method=="GET":
        return render(request, 'staff/add_facture.html', {'clients':affiche_client})
    elif request.method=="POST":
        designation=request.POST.get("designation")
        poids_en_grammes=request.POST.get("poids_en_grammes")
        titre_en_caract=request.POST.get("titre_en_caract")
        prix_unitaire=request.POST.get("prix_unitaire")
        # barre0=request.POST.get("barre0")
        # barre1=request.POST.get("barre1")
        # barre2=request.POST.get("barre2")
        clients_id=request.POST.get("client_id")
        try:
            facture=Facture(designation=designation,poids_en_grammes=poids_en_grammes,titre_en_caract=titre_en_caract,prix_unitaire=prix_unitaire,client_id=clients_id)
            facture.save()
            messages.success(request,"Ajout avec Success")
            return HttpResponseRedirect(reverse("index_staff"))
        except Exception as e :
            messages.error(request, "Pas d'ajout " + str(e))
            print(e)
            return HttpResponseRedirect(reverse("index_staff"))


def ajouter_ba(request,client_id):
    affiche_client=Client.objects.get(id=client_id)

    if request.method=="GET":
        return render(request, 'staff/add_ba.html', {'clients':affiche_client})
    elif request.method=="POST":
        numero_ordre=request.POST.get("numero_ordre")
        parametre=request.POST.get("parametre")
        type_echantillon=request.POST.get("type_echantillon")
        clients_id=request.POST.get("client_id")
        try:
            ba=BordereauAdministratif(numero_ordre=numero_ordre,parametre=parametre,type_echantillon=type_echantillon,client_id=clients_id)
            ba.save()
            messages.success(request,"Ajout avec Success")
            return HttpResponseRedirect(reverse("index_staff"))
        except Exception as e :
            messages.error(request, "Pas d'ajout " + str(e))
            print(e)
            return HttpResponseRedirect(reverse("index_staff"))




def do_login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("acceuil"))
            
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("index_staff"))
            else:
                return HttpResponse("dingo")

        else:
            messages.error(request,"Email ou mot de passe invalide")
            return HttpResponseRedirect("/")


# @login_required(login_url="/")
def nouveau_client(request):
    return render(request, 'staff/add_client.html')

def add_staff(request):
    return render(request, 'administrateur/add_staff.html')


# def modifier_client(request):
#     return render(request, 'administrateur/modifier_client.html')

def do_client(request):
    if request.method!="POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        prenom=request.POST.get("prenom")
        nom=request.POST.get("nom")
        telephone=request.POST.get("telephone")
        adresse=request.POST.get("adresse")
        email=request.POST.get("email")
        sexe=request.POST.get("sexe")
        

        try:
            client=Client(prenom=prenom,nom=nom,telephone=telephone,adresse=adresse,email=email,sexe=sexe)
            client.save()
            messages.success(request,"Ajout avec Success")
            return HttpResponseRedirect(reverse("index_staff"))
        except:
            messages.error(request,"Echec de l'ajout")
            return HttpResponseRedirect(reverse("client"))



def do_staff(request):
    if request.method!="POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
            first_name = request.POST.get('prenom')
            last_name = request.POST.get('nom')
            username = request.POST.get('username')
            address = request.POST.get('adresse')
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = CustomUser.objects.create_user(
                   username=username, email=email, password=password, user_type=2, first_name=first_name, last_name=last_name)
                user.address = address
                user.save()
                messages.success(request, "Ajout avec Success")
                return redirect(reverse('index'))

            except Exception as e:
                messages.error(request, "Pas d'ajout " + str(e))

    return render(request, 'administrateur/add_staff.html')


def delete_client(request, client_id):
    clients = get_object_or_404(Client, id=client_id)
    clients.delete()
    messages.success(request, "Client Supprimer avec success!")
    return redirect(reverse('index'))


# def do_facture(request):
#     if request.method!="POST":
#             return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         designation=request.POST.get("designation")
#         date=request.POST.get("date")
#         poids_en_grammes=request.POST.get("poids_en_grammes")
#         titre_en_caract=request.POST.get("titre_en_caract")
#         prix_unitaire=request.POST.get("prix_unitaire")
#         client_id=request.POST.get("client_id")
        

#         try:
#             facture=Facture(designation=designation,date=date,poids_en_grammes=poids_en_grammes,titre_en_caract=titre_en_caract,prix_unitaire=prix_unitaire,client_id=client_id)
#             facture.save()
#             messages.success(request,"Ajout avec Success")
#             return HttpResponseRedirect(reverse("index_staff"))
#         except Exception as e :
#             messages.error(request, "Pas d'ajout " + str(e))
#             print(e)
#             return HttpResponseRedirect(reverse("index_staff"))




# def up_client(request, client_id):
#     clients = get_object_or_404(Client, id=client_id)

#     # clients=Client.objects.all()
#     # form = CourseForm(request.POST or None, instance=instance)
#     # context = {
#     #     'form': form,
#     #     'course_id': course_id,
#     #     'page_title': 'Editer Classe'
#     # }
#     if request.method == 'POST':

#             prenom=request.POST.get("prenom")
#             nom=request.POST.get("nom")
#             telephone=request.POST.get("telephone")
#             adresse=request.POST.get("adresse")
#             email=request.POST.get("email")
#             sexe=request.POST.get("sexe")
#             try:
#                 clients = Client.objects.get(id=client_id)
#                 clients.prenom = prenom
#                 clients.nom = nom
#                 clients.telephone = telephone
#                 clients.adresse = adresse
#                 clients.email = email
#                 clients.sexe = sexe
#                 clients.save()
#                 messages.success(request, "Mise a jour avec Success")
#             except:
#                 messages.error(request, "Echec mise a jour")

#     return render(request, 'administrateur/modifier_client.html')


def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect(reverse("login"))