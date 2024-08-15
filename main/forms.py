from django import forms
from .models import Profil, Publication

class PubForm(forms.ModelForm):
    profil= forms.ModelChoiceField(queryset= Profil.objects.all(), label="Moi")

    class Meta:
        model= Publication

        fields= ['legend', 'image_1']
        labels ={'legend': 'Ecrire quelque chose', 'image_1': 'Entrer une photo'}
    