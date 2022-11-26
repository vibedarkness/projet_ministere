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



def login(request):
    return render(request, 'administrateur/login.html')


# @login_required(login_url="/")
def voir(request):
    return render(request, 'administrateur/voir.html')

def voir_staff(request):
    return render(request, 'staff/voir.html')



def do_login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("index"))
            
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

def nouveau_facture(request):
    return render(request, 'staff/add_facture.html')

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



def up_client(request, client_id):
    clients = get_object_or_404(Client, id=client_id)

    # clients=Client.objects.all()
    # form = CourseForm(request.POST or None, instance=instance)
    # context = {
    #     'form': form,
    #     'course_id': course_id,
    #     'page_title': 'Editer Classe'
    # }
    if request.method == 'POST':

            prenom=request.POST.get("prenom")
            nom=request.POST.get("nom")
            telephone=request.POST.get("telephone")
            adresse=request.POST.get("adresse")
            email=request.POST.get("email")
            sexe=request.POST.get("sexe")
            try:
                clients = Client.objects.get(id=client_id)
                clients.prenom = prenom
                clients.nom = nom
                clients.telephone = telephone
                clients.adresse = adresse
                clients.email = email
                clients.sexe = sexe
                clients.save()
                messages.success(request, "Mise a jour avec Success")
            except:
                messages.error(request, "Echec mise a jour")

    return render(request, 'administrateur/modifier_client.html')



def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect(reverse("login"))