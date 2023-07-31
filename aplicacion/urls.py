from django.urls import path,include
from .views import *

urlpatterns = [
    path('inicio/',inicio),
    path('crear_objeto/',crearobjeto,name='crearobjeto'),
    path('maquinas/',maquinas,name='maquinas'),
    path('implementos/',implementos,name='implementos'),
    path('suplementos/',suplementos,name='suplementos'),
    path('buscarobjeto/',buscarobjeto,name='buscarobjeto'),
    path('encontrarobjeto/',encontrarobjeto,name='encontrar')
]
