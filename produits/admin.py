from django.contrib import admin
from .models import Produit, Commande, ArticleCommande


admin.site.register(Produit)


class ArticleCommandeInline(admin.TabularInline):
    model = ArticleCommande
    extra = 0


class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'email', 'date_commande', 'payee']
    inlines = [ArticleCommandeInline]


admin.site.register(Commande, CommandeAdmin)
