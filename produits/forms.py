from django import forms
from .models import Commande


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom', 'email', 'adresse', 'ville', 'code_postal', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom complet'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Adresse e-mail'}),
            'adresse': forms.TextInput(attrs={'placeholder': 'Adresse'}),
            'ville': forms.TextInput(attrs={'placeholder': 'Ville'}),
            'code_postal': forms.TextInput(attrs={'placeholder': 'Code postal'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Téléphone (optionnel)'}),
        }