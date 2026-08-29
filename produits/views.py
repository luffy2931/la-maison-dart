from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from .panier import Panier
from .forms import CommandeForm
from .models import Commande, ArticleCommande


def accueil(request):
    produits = Produit.objects.all()
    return render(request, 'produits/accueil.html', {
        'produits': produits
    })


def detail_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    return render(request, 'produits/detail.html', {
        'produit': produit
    })


def ajouter_au_panier(request, id):
    panier = Panier(request)
    produit = get_object_or_404(Produit, id=id)
    panier.ajouter(produit)
    return redirect('voir_panier')


def supprimer_du_panier(request, id):
    panier = Panier(request)
    produit = get_object_or_404(Produit, id=id)
    panier.supprimer(produit)
    return redirect('voir_panier')


def voir_panier(request):
    panier = Panier(request)
    return render(request, 'produits/panier.html', {'panier': panier})


def passer_commande(request):
    panier = Panier(request)

    if len(panier) == 0:
        return redirect('voir_panier')

    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save()
            for item in panier:
                produit = item['produit']
                ArticleCommande.objects.create(
                    commande=commande,
                    produit=produit,
                    prix=produit.prix,
                    quantite=item['quantite']
                )
                produit.stock -= item['quantite']
                produit.save()

            panier.vider()
            return render(request, 'produits/commande_confirmee.html', {'commande': commande})
    else:
        form = CommandeForm()

    return render(request, 'produits/commande.html', {'form': form, 'panier': panier})


def a_propos(request):
    return render(request, 'produits/a_propos.html')