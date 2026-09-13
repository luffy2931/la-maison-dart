from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('tableau/<int:id>/', views.detail_produit, name='detail_produit'),
    path('panier/ajouter/<int:id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/supprimer/<int:id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('commande/', views.passer_commande, name='passer_commande'),
    path('a-propos/', views.a_propos, name='a_propos'),
    path('contact/', views.contact, name='contact'),
]