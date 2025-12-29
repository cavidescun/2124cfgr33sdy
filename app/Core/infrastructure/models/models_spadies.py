from django.db import models


class TasaDesercionIES(models.Model):
    """Tabla de tasas de deserción por IES del SPADIES"""
    
    id = models.AutoField(primary_key=True)
    codigo_ies_padre = models.IntegerField(null=False)
    nombre_ies = models.CharField(max_length=300, null=False)
    año = models.IntegerField(null=False, db_column='año')
    tasa_desercion = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    fecha_carga = models.DateTimeField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = '"SPADIES"."tda_ies_padre_total"'
        verbose_name = 'Tasa de Deserción IES'
        verbose_name_plural = 'Tasas de Deserción IES'

    def __str__(self):
        return f"{self.nombre_ies} - {self.año}: {self.tasa_desercion}%"