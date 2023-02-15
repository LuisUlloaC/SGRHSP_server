from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from Tesis import utils
from server.serializers import *


class CatOcupacionalView(viewsets.ModelViewSet):
    serializer_class = CatOcupSerializer
    queryset = CategoriaOcupacional.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                CategoriaOcupacional.objects.get(pk=object.get('id')).delete()
            return Response({'CatOcup Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('CatOcup')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class GrupoEscView(viewsets.ModelViewSet):
    serializer_class = GrupoEscalaSerializer
    queryset = GrupoEscala.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                GrupoEscala.objects.get(pk=object.get('id')).delete()
            return Response({'GrupoEsc Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('GrupoEsc')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class ClasificacionView(viewsets.ModelViewSet):
    serializer_class = ClasSerializer
    queryset = Clasificacion.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                Clasificacion.objects.get(pk=object.get('id')).delete()
            return Response({'Clasificacion Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('GrupoEsc')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class NivelPreparacionView(viewsets.ModelViewSet):
    serializer_class = NivPrepSerializer
    queryset = NivelPreparacion.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                NivelPreparacion.objects.get(pk=object.get('id')).delete()
            return Response({'NivelPrep Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('GruNivelPrep')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class FuenteProcedenciaView(viewsets.ModelViewSet):
    serializer_class = FuenteProcSerializer
    queryset = FuenteProcedencia.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                FuenteProcedencia.objects.get(pk=object.get('id')).delete()
            return Response({'FuenteProc Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('FuenteProc')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class MotivoBajaView(viewsets.ModelViewSet):
    serializer_class = MotBajaSerializer
    queryset = MotivoBaja.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                MotivoBaja.objects.get(pk=object.get('id')).delete()
            return Response({'MotivoBaja Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('GrupoEsc')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class MunicipioView(viewsets.ModelViewSet):
    serializer_class = MunSerializer
    queryset = Municipio.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                Municipio.objects.get(pk=object.get('id')).delete()
            return Response({'Municipio Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('GrupoEsc')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class UnidadView(viewsets.ModelViewSet):
    serializer_class = UnidadSerializer
    queryset = Unidad.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                Unidad.objects.get(pk=object.get('id')).delete()
            return Response({'Unidad Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('GrupoEsc')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class UnidadOrganizativaView(viewsets.ModelViewSet):
    serializer_class = UnidadOrganizativaSerializer
    queryset = UnidadOrganizativa.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                UnidadOrganizativa.objects.get(pk=object.get('id')).delete()
            return Response({'UnidadOrg Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('GrupoEsc')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class CargoView(viewsets.ModelViewSet):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                Cargo.objects.get(pk=object.get('id')).delete()
            return Response({'Cargo Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('Cargo')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class PlazaView(viewsets.ModelViewSet):
    serializer_class = PlazaSerializer
    queryset = Plaza.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                Plaza.objects.get(pk=object.get('id')).delete()
            return Response({'Plaza Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('Cargo')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class PersonalView(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for object in request.data:
                Personal.objects.get(pk=object.get('id')).delete()
            return Response({'Cargo Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('Cargo')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all().order_by('-pk')
    serializer_class = ProvSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def delete(self, request):
        try:
            for province in request.data:
                Provincia.objects.get(pk=province.get('id')).delete()
            return Response({'Provincias Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('Provincia')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
