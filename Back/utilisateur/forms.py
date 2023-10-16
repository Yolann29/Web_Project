from django import forms
from .models import companies  # Assurez-vous d'importer votre modèle companies

class SelectCompanyForm(forms.Form):
    company = forms.ModelChoiceField(
        queryset=companies.objects.all(),
        label="Sélectionnez une entreprise"
    )
