from app.Core.infrastructure.sqlserver_base import SQLServerBaseModel
from django.db import models
class ProfesorSQLServer(SQLServerBaseModel):
    id_profesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=150)

    class Meta(SQLServerBaseModel.Meta):
        db_table = "Profesores"
