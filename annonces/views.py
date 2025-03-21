from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , get_object_or_404
from .models import Categorie, Annonce
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import re


def list_annonces(request):
    categories = Categorie.objects.all()
    annonces = Annonce.objects.filter(statut="Acceptée")

    context = {
        "categories": categories,
        "annonces": annonces
    }

    return render(request, "list_annonces.html", context)

@login_required
def Publie_Annonce(request):
    categories = Categorie.objects.all()
    annonces = Annonce.objects.filter(utilisateur_id=request.user.id)
    if request.method == "POST":
        titre = request.POST["titre"]
        description = request.POST["description"]
        categorie = Categorie.objects.get(id=request.POST["categorie"])
        image = request.FILES["image"]
        annonce = Annonce.objects.create(
            titre=titre,
            description=description,
            categorie=categorie,
            image=image,
            utilisateur=request.user ,
            statut = "attente"
        )
        return redirect("list_annonces")

    return render(request, "publie_Annonce.html", {"categories": categories})


def mes_annonces(request):
    annonces = Annonce.objects.filter(utilisateur=request.user)

    return render(request, "Mes_Annonces.html", {"annonces": annonces})

def suprimer_Annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)
    annonce.delete()
    return redirect("mes_annonces")

@login_required
def modifier_annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id, utilisateur=request.user)
    categories = Categorie.objects.all()

    if request.method == "POST":
        annonce.titre = request.POST["titre"]
        annonce.description = request.POST["description"]
        annonce.categorie = Categorie.objects.get(id=request.POST["categorie"])

        if "image" in request.FILES:
            annonce.image = request.FILES["image"]

        annonce.statut = "attente"
        annonce.save()
        return redirect("mes_annonces")

    return render(request, "modifier_annonce.html", {"annonce": annonce, "categories": categories})


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        is_admin = request.POST.get("is_admin", False)

        if User.objects.filter(username=username).exists():
            messages.error(request, "Le nom d’utilisateur existe déjà. Veuillez en choisir un autre.")
            return redirect("signup")


        if len(password) < 8 or not re.search(r"[A-Za-z]", password) or not re.search(r"[0-9]", password):
            messages.error(request, "Le mot de passe doit comporter au moins 8 caractères et contenir des lettres et des chiffres.")
            return redirect("signup")


        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect("signup")
        user = User.objects.create_user(username=username, password=password)
        if is_admin:
            user.is_staff = True
        user.save()

        messages.success(request, "votre counte a ete cree avec success!")
        return redirect("login")

    return render(request, "signup.html")
def is_admin(user):
    return user.is_staff

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("list_annonces")
        else:
            messages.error(request, "password ou nom invalidee.")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def admin_annonces(request):
    if not request.user.is_staff:
        return redirect("list_annonces")

    annonces = Annonce.objects.filter(statut="attente")
    return render(request, "admin_annonces.html", {"annonces": annonces})
@login_required
@user_passes_test(is_admin)
def change_status(request, annonce_id, status):
    annonce = Annonce.objects.get(id=annonce_id)
    if status in ["Acceptée", "Rejetée"]:
        annonce.statut = status
        annonce.save()
    return redirect("admin_annonces")
@login_required
def admin_dashboard(request):
    return redirect('/admin/')