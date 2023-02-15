from django.contrib.auth.models import AbstractUser
from django.db import models


class CategoriaOcupacional(models.Model):
    nombre = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Categoria Ocupacional"
        verbose_name_plural = "Categorias Ocupacionales"

    def __str__(self):
        return self.nombre


class GrupoEscala(models.Model):
    nombre = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Grupo Escala"

    def __str__(self):
        return self.nombre


class Clasificacion(models.Model):
    nombre = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Clasificacion"
        verbose_name_plural = "Clasificaciones"

    def __str__(self):
        return self.nombre


class NivelPreparacion(models.Model):
    nombre = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Nivel de Preparacion"
        verbose_name_plural = "Niveles de Preparacion"

    def __str__(self):
        return self.nombre


class FuenteProcedencia(models.Model):
    nombre = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Fuente de Procedencia"
        verbose_name_plural = "Fuentes de Procedencia"

    def __str__(self):
        return self.nombre


class MotivoBaja(models.Model):
    nombre = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Motivo de Baja"

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=300)
    provincia = models.ForeignKey(Provincia,
                                  on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    nombre = models.CharField(max_length=300)
    municipio = models.ForeignKey(Municipio,
                                  on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.nombre


class UnidadOrganizativa(models.Model):
    nombre = models.CharField(max_length=300)
    unidad = models.ForeignKey(Unidad,
                               on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Unidad Organizativa"
        verbose_name_plural = "Unidades Organizativas"

    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=300)
    categoriaOcupacional = models.ForeignKey(CategoriaOcupacional,
                                             on_delete=models.DO_NOTHING)
    grupoEscala = models.ForeignKey(GrupoEscala,
                                    on_delete=models.DO_NOTHING)
    clasificacion = models.ForeignKey(Clasificacion,
                                      on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.nombre


class Plaza(models.Model):
    nombre = models.CharField(max_length=300)
    cantidad = models.IntegerField()
    necesarios = models.IntegerField()
    cubiertas = models.IntegerField()
    mision = models.IntegerField()
    unidadOrganizativa = models.ForeignKey(UnidadOrganizativa,
                                           on_delete=models.DO_NOTHING)
    cargo = models.ForeignKey(Cargo,
                              on_delete=models.DO_NOTHING)
    nivelPreparacion = models.ForeignKey(NivelPreparacion,
                                         on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Plaza"
        verbose_name_plural = "Plazas"

    def __str__(self):
        return self.nombre


class Personal(models.Model):
    nombre = models.CharField(max_length=300)
    apellidos = models.CharField(max_length=300)
    sexo = models.CharField(max_length=9)
    ci = models.CharField(max_length=11)
    direccionParticular = models.CharField(max_length=1000)
    fechaAlta = models.DateField()
    fechaBaja = models.DateField()
    fuenteProcedencia = models.ForeignKey(FuenteProcedencia,
                                          on_delete=models.DO_NOTHING)
    motivoBaja = models.ForeignKey(MotivoBaja,
                                   on_delete=models.DO_NOTHING)
    plaza = models.ForeignKey(Plaza,
                              on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return self.nombre
