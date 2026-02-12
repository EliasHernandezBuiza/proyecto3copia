from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="inicio"),
    path('blog',listado,name="blog"),
    path('entrada/crear',crea_entrada,name="crea_entrada")
]
# nombre de la ruta de registro