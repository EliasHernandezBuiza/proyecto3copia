from django import forms
from .models import Entrada

class FormularioEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('categoria', 'titulo', 'contenido', 'imagen')