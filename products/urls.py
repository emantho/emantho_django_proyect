from django.urls import path
from . import views # se deja en "." por estan en el mismo directorio y para evitar problemas con otros drectorios

urlpatterns = [
    # queda '' blanco por ser la raiz de la pagina PRODUCTOS
    path('', views.index), # Se enlaza con la funcion index del modulo views.py
    path('new', views.new)


]