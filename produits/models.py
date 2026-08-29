from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
class Commande(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    adresse = models.CharField(max_length=250)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20)
    telephone = models.CharField(max_length=30, blank=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    payee = models.BooleanField(default=False)

    def __str__(self):
        return f"Commande {self.id} - {self.nom}"

    def total(self):
        return sum(item.prix_total() for item in self.articles.all())


class ArticleCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='articles', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField(default=1)

    def prix_total(self):
        return self.prix * self.quantite
