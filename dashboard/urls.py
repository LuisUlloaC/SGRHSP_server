from django.urls import path
from .views import *

urlpatterns = [
    path('getMainNumbers/', getMainNumbers),
    path('getTrabajadoresXClasificacion/', getTrabajadoresXClasificacion),
    path('getMunicipioXClasificacion/', getMunicipioXClasificacion),
    path('getCatOcupXTrab/', getCatOcupXTrab),
    path('getNivPrepXTrab/', getNivPrepXTrab),
    path('getUnidadOrgXNivPrep/', getUnidadOrgXNivPrep),
]