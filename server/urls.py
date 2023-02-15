from django.urls import path, re_path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'cat_ocupacional', CatOcupacionalView, 'Categoria ocupacional')
router.register(r'grup_esc', GrupoEscView, 'Grupo escala')
router.register(r'clasificacion', ClasificacionView, 'Clasificacion')
router.register(r'fuente_proc', FuenteProcedenciaView, 'Fuente de Procedencia')
router.register(r'motivo_baja', MotivoBajaView, 'Motivo Baja')
router.register(r'provincias', ProvinceViewSet, 'Provincia')
router.register(r'municipio', MunicipioView, 'Municipio')
router.register(r'unidad', UnidadView, 'Unidad')
router.register(r'nivel_preparacion', NivelPreparacionView, 'Nivel Preparacion')
router.register(r'unidad_organizativa', UnidadOrganizativaView, 'Unidad Organizativa')
router.register(r'cargo', CargoView, 'Cargo')
router.register(r'plaza', PlazaView, 'Plaza')
router.register(r'personal', PersonalView, 'Personal')

urlpatterns = [
    path('', include(router.urls)),

]
