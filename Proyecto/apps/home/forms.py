from django import forms
from . import models

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        exclude = ['user']
