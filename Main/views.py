from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from Main.EmailBackend import EmailBackend
from Main.models import Client

# Create your views here.


# @login_required(login_url="/")
def index(request):
    clients=Client.objects.all()
    return render(request, 'administrateur/index.html',{"clients":clients})



def login(request):
    return render(request, 'administrateur/login.html')


# @login_required(login_url="/")
def voir(request):
    return render(request, 'administrateur/voir.html')



def do_login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("dingo")

        else:
            messages.error(request,"Email ou mot de passe invalide")
            return HttpResponseRedirect("/")


# @login_required(login_url="/")
def nouveau_client(request):
    return render(request, 'administrateur/add_client.html')

def nouveau_facture(request):
    return render(request, 'administrateur/add_facture.html')

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
            return HttpResponseRedirect(reverse("index"))
        except:
            messages.error(request,"Echec de l'ajout")
            return HttpResponseRedirect(reverse("client"))



def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect(reverse("login"))