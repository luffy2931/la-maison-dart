from .models import Produit


class Panier:
    def __init__(self, request):
        self.session = request.session
        panier = self.session.get('panier')
        if not panier:
            panier = self.session['panier'] = {}
        self.panier = panier

    def ajouter(self, produit):
        id_produit = str(produit.id)
        if produit.stock <= 0:
            return
        if id_produit not in self.panier:
            self.panier[id_produit] = {'quantite': 1}
        else:
            if self.panier[id_produit]['quantite'] < produit.stock:
                self.panier[id_produit]['quantite'] += 1
        self.sauvegarder()

    def supprimer(self, produit):
        id_produit = str(produit.id)
        if id_produit in self.panier:
            del self.panier[id_produit]
            self.sauvegarder()

    def sauvegarder(self):
        self.session.modified = True

    def __iter__(self):
        ids_produits = self.panier.keys()
        produits = Produit.objects.filter(id__in=ids_produits)
        for produit in produits:
            self.panier[str(produit.id)]['produit'] = produit

        for item in self.panier.values():
            item['prix_total'] = item['produit'].prix * item['quantite']
            yield item

    def __len__(self):
        return sum(item['quantite'] for item in self.panier.values())

    def total(self):
        return sum(item['produit'].prix * item['quantite'] for item in self)

    def vider(self):
        del self.session['panier']
        self.sauvegarder()