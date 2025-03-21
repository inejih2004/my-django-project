from django.contrib import admin
from .models import Annonce,Categorie
admin.site.register(Annonce)

admin.site.register(Categorie)


def site():
    return None