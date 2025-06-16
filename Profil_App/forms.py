from  django import forms
from .models import Profil_Model


class Profil_Form(forms.ModelForm):
    class Meta:
        model = Profil_Model
        fields = '__all__'