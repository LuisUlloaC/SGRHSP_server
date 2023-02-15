from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from server.models import *

from server.models import Personal


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMainNumbers(request):

    try:
        response = {
            'users': get_user_model().objects.all().count(),
            'personal': Personal.objects.filter(motivoBaja=1).count()
        }
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTrabajadoresXClasificacion(request):
    response = []
    id = 0
    for clasificacion in Clasificacion.objects.all():
        nombre = clasificacion.nombre
        cantidadTrabajadores = 0
        for cargo in Cargo.objects.all():
            for plaza in Plaza.objects.all():
                for personal in Personal.objects.all():
                    if str(clasificacion.nombre) == str(cargo.clasificacion) and str(plaza.cargo) == str(cargo.nombre) and str(personal.plaza) == str(plaza.nombre):
                        cantidadTrabajadores += 1
        response.append({"id":id, "nombre": nombre, "cantidad": cantidadTrabajadores})
        id += 1
    try: 
        response
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMunicipioXClasificacion(request):
    response = []
    id = 0
    for municipio in Municipio.objects.all():
        nombre = municipio.nombre
        cantidad = 0
        for unidad in Unidad.objects.all():
            for unidadOrg in UnidadOrganizativa.objects.all():
                for plaza in Plaza.objects.all():
                    for cargo in Cargo.objects.all():
                        for clasificacion in Clasificacion.objects.all():
                            if str(unidad.municipio) == str(municipio.nombre) and str(unidad.nombre) == str(unidadOrg.unidad) and str(plaza.unidadOrganizativa) == str(unidadOrg.nombre) and str(plaza.cargo) == str(cargo.nombre) and str(cargo.clasificacion) == str(clasificacion.nombre):
                                cantidad += 1
        response.append({"id":id, "nombre": nombre, "cantidad": cantidad})
        id += 1
    try: 
        response
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCatOcupXTrab(request):
    response = []
    id = 0
    for catOcup in CategoriaOcupacional.objects.all():
        nombre = catOcup.nombre
        cantidad = 0
        for cargo in Cargo.objects.all():
            for plaza in Plaza.objects.all():
                for personal in Personal.objects.all():
                    if str(cargo.categoriaOcupacional) == str(catOcup.nombre) and str(cargo.nombre) == str(plaza.cargo) and str(plaza.nombre) == str(personal.plaza):
                        cantidad += 1
        response.append({"id":id, "nombre": nombre, "cantidad": cantidad})
        id += 1
    try: 
        response
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNivPrepXTrab(request):
    response = []
    id = 0
    for nivPrep in NivelPreparacion.objects.all():
        nombre = nivPrep.nombre
        cantidad = 0
        for plaza in Plaza.objects.all():
            for personal in Personal.objects.all():
                if str(plaza.nivelPreparacion) == str(nivPrep.nombre) and str(personal.plaza) == str(plaza.nombre):
                    cantidad += 1
        response.append({"id":id, "nombre": nombre, "cantidad": cantidad})
        id += 1
    try: 
        response
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUnidadOrgXNivPrep(request):
    response = []
    id = 0
    for unidadOrg in UnidadOrganizativa.objects.all():
        nombre = unidadOrg.nombre
        cantidad = 0
        for nivPrep in NivelPreparacion.objects.all():
            for plaza in Plaza.objects.all():
                for personal in Personal.objects.all():
                    if str(plaza.unidadOrganizativa) == str(unidadOrg.nombre) and str(plaza.nivelPreparacion) == str(nivPrep.nombre) and str(personal.plaza) == str(plaza.nombre):
                        cantidad += 1
        response.append({"id":id, "nombre": nombre, "cantidad": cantidad})
        id += 1
    try: 
        response
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)