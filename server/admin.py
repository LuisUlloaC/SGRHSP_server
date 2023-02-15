from django.contrib import admin
from server.models import *


@admin.register(CategoriaOcupacional)
class CatOcupAdmin(admin.ModelAdmin):
    pass


@admin.register(GrupoEscala)
class GrupoEscAdmin(admin.ModelAdmin):
    pass


@admin.register(Clasificacion)
class ClasAdmin(admin.ModelAdmin):
    pass


@admin.register(NivelPreparacion)
class NivelPrepAdmin(admin.ModelAdmin):
    pass


@admin.register(FuenteProcedencia)
class FuenteProcAdmin(admin.ModelAdmin):
    pass


@admin.register(MotivoBaja)
class MotivoBajaAdmin(admin.ModelAdmin):
    pass


@admin.register(Provincia)
class ProvAdmin(admin.ModelAdmin):
    pass


@admin.register(Municipio)
class MunAdmin(admin.ModelAdmin):
    pass


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    pass


@admin.register(UnidadOrganizativa)
class UnidadOrganizativaAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass


@admin.register(Plaza)
class PlazaAdmin(admin.ModelAdmin):
    pass


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    pass
