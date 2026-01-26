from django.shortcuts import render
from forms import FormularioEntrada

# Create your views here.

def crea_entrada(request):
    form = FormularioEntrada()
    return render(request, "creaEntrada.html",{"form":form})