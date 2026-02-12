
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Entrada
from .forms import FormularioEntrada
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")


def listado(request):
    #vamos a obtener todas las entradas
    entradas= Entrada.objects.all()
    return render(request,"blog.html",{"entradas": entradas})
    # envio las entradas como un diccionario


def crea_entrada(request):
    if request.method == "POST":
        form = FormularioEntrada(request.POST, request.FILES)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.autor_id = request.user.id 
            entrada.save()
            titulo = form.cleaned_data.get("titulo")
            messages.success(request,f"la entrada {titulo} es correcta")
            return redirect("blog")
        else:
            for msg in form.error_messages:
                 messages.error(request,form.error_messages[msg])

    form= FormularioEntrada()
    return render(request,"creaEntrada.html",{"form": form})