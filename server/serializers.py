from rest_framework import serializers
from server.models import *


class CatOcupSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)

    class Meta:
        model= CategoriaOcupacional
        fields = '__all__'


class GrupoEscalaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)

    class Meta:
        model = GrupoEscala
        fields = '__all__'


class ClasSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)

    class Meta:
        model = Clasificacion
        fields = '__all__'


class NivPrepSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)

    class Meta:
        model = NivelPreparacion
        fields = '__all__'


class FuenteProcSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)

    class Meta:
        model = FuenteProcedencia
        fields = '__all__'


class MotBajaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)

    class Meta:
        model = MotivoBaja
        fields = '__all__'


class ProvSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)

    class Meta:
        model = Provincia
        fields = '__all__'


class MunSerializer(serializers.ModelSerializer):
    nombre_provincia = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Municipio
        fields = '__all__'

    def get_nombre_provincia(self, obj):
        return obj.provincia.nombre


class UnidadSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)
    nombre_municipio = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Unidad
        fields = '__all__'

    def get_nombre_municipio(self, obj):
        return obj.municipio.nombre


class UnidadOrganizativaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)
    nombre_unidad = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UnidadOrganizativa
        fields = '__all__'

    def get_nombre_unidad(self, obj):
        return obj.unidad.nombre


class CargoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)
    nombre_catOcup = serializers.SerializerMethodField(read_only=True)
    nombre_grupoEscala = serializers.SerializerMethodField(read_only=True)
    nombre_clasificacion = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cargo
        fields = '__all__'

    def get_nombre_catOcup(self, obj):
        return obj.categoriaOcupacional.nombre

    def get_nombre_grupoEscala(self, obj):
        return obj.grupoEscala.nombre

    def get_nombre_clasificacion(self, obj):
        return obj.clasificacion.nombre


class PlazaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)
    nombre_unidadOrganizativa = serializers.SerializerMethodField(read_only=True)
    nombre_cargo = serializers.SerializerMethodField(read_only=True)
    nombre_nivelPreparacion = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Plaza
        fields = '__all__'

    def get_nombre_unidadOrganizativa(self, obj):
        return obj.unidadOrganizativa.nombre

    def get_nombre_cargo(self, obj):
        return obj.cargo.nombre

    def get_nombre_nivelPreparacion(self, obj):
        return obj.nivelPreparacion.nombre


class PersonalSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)
    nombre_fuenteProcedencia = serializers.SerializerMethodField(read_only=True)
    nombre_motivoBaja = serializers.SerializerMethodField(read_only=True)
    nombre_plaza = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Personal
        fields = '__all__'

    def get_nombre_fuenteProcedencia(self, obj):
        return obj.fuenteProcedencia.nombre

    def get_nombre_motivoBaja(self, obj):
        return obj.fuenteProcedencia.nombre

    def get_nombre_plaza(self, obj):
        return obj.plaza.nombre
