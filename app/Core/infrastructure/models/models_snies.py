"""
Modelos Django para el esquema SNIES
Base de datos: registro_calificado
Esquema: SNIES
Generado automáticamente a partir de la estructura de las tablas
"""

from django.db import models


class CampoAmplio(models.Model):
    id_amplio = models.CharField(
        max_length=255,
        primary_key=True
    )
    nombre_amplio = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table =  db_table = '"SNIES"."campo_amplio"'
        verbose_name = 'Campo Amplio'
        verbose_name_plural = 'Campos Amplios'

    def __str__(self):
        return f"{self.id_amplio} - {self.id_amplio}"

class ConsolidadoEducacionSuperior(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')  # Django necesita un PK    
    anio = models.IntegerField(null=True, blank=True)
    semestre = models.IntegerField(null=True, blank=True)
    codigo_institucion = models.IntegerField(null=True, blank=True)
    institucion = models.CharField(max_length=255, null=True, blank=True)
    codigo_snies_programa = models.IntegerField(null=True, blank=True)
    programa_academico = models.CharField(max_length=255, null=True, blank=True)
    nivel_formacion = models.CharField(max_length=100, null=True, blank=True)
    modalidad = models.CharField(max_length=100, null=True, blank=True)
    departamento_programa = models.CharField(max_length=100, null=True, blank=True)
    municipio_programa = models.CharField(max_length=100, null=True, blank=True)
    total_inscritos = models.IntegerField(default=0)
    total_admitidos = models.IntegerField(default=0)
    total_matriculados = models.IntegerField(default=0)
    total_graduados = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = '"SNIES"."consolidado_educacion_superior_snies"'
        verbose_name = 'Consolidado Educación Superior'
        verbose_name_plural = 'Consolidado Educación Superior'

    def __str__(self):
        return f"{self.institucion} - {self.programa_academico} ({self.anio})"
class ProgramaAcademico(models.Model):
    """Tabla de programas académicos del SNIES"""
    id = models.AutoField(primary_key=True)
    codigo_institucion_padre = models.CharField(max_length=50, null=True, blank=True)
    codigo_institucion = models.CharField(max_length=50, null=True, blank=True)
    nombre_institucion = models.CharField(max_length=500, null=True, blank=True)
    estado_institucion = models.CharField(max_length=100, null=True, blank=True)
    caracter_academico = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=50, null=True, blank=True)
    registro_unico = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True
    )
    codigo_snies_del_programa = models.DecimalField(
        max_digits=10, decimal_places=0
    )
    codigo_anterior_icfes = models.CharField(max_length=100, null=True, blank=True)
    nombre_del_programa = models.CharField(max_length=500, null=True, blank=True)
    titulo_otorgado = models.CharField(max_length=500, null=True, blank=True)
    estado_programa = models.CharField(max_length=100, null=True, blank=True)
    justificacion = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True
    )
    justificacion_detallada = models.TextField(null=True, blank=True)
    reconocimiento_del_ministerio = models.CharField(
        max_length=200, null=True, blank=True
    )
    resolucion_de_aprobacion = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True
    )
    fecha_de_resolucion = models.DateField(null=True, blank=True)
    fecha_ejecutoria = models.DateField(null=True, blank=True)
    vigencia_años = models.CharField(max_length=50, null=True, blank=True)
    fecha_de_registro_en_snies = models.DateTimeField(null=True, blank=True)
    cine_f_2013_ac_campo_amplio = models.CharField(
        max_length=200, null=True, blank=True
    )
    cine_f_2013_ac_campo_especifico = models.CharField(
        max_length=200, null=True, blank=True
    )
    cine_f_2013_ac_campo_detallado = models.CharField(
        max_length=200, null=True, blank=True
    )
    area_de_conocimiento = models.CharField(max_length=200, null=True, blank=True)
    nucleo_basico_del_conocimiento = models.CharField(
        max_length=200, null=True, blank=True
    )
    nivel_academico = models.CharField(max_length=100, null=True, blank=True)
    nivel_de_formacion = models.CharField(max_length=100, null=True, blank=True)
    modalidad = models.CharField(max_length=100, null=True, blank=True)
    numero_creditos = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True
    )
    numero_periodos_de_duracion = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True
    )
    periodicidad = models.CharField(max_length=100, null=True, blank=True)
    se_ofrece_por_ciclos_propedeuticos = models.CharField(
        max_length=10, null=True, blank=True
    )
    periodicidad_admisiones = models.CharField(max_length=100, null=True, blank=True)
    programa_en_convenio = models.CharField(max_length=10, null=True, blank=True)
    departamento_oferta_programa = models.CharField(
        max_length=100, null=True, blank=True
    )
    municipio_oferta_programa = models.CharField(max_length=100, null=True, blank=True)
    costo_matricula_estud_nuevos = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, blank=True
    )
    vigencia_transitoria = models.CharField(max_length=200, null=True, blank=True)
    observacion_decreto_1174_23 = models.TextField(null=True, blank=True)
    fecha_carga = models.DateTimeField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    fila_excel = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = '"SNIES"."snies_programas_academicos"'
        verbose_name = "Programa Académico"
        verbose_name_plural = "Programas Académicos"

    def __str__(self):
        return f"{self.codigo_snies_del_programa} - {self.nombre_del_programa}"
    

