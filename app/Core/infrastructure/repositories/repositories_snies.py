from django.db.models import (
    Q, Case, When, IntegerField, Value, Max, F
)
from app.Core.domain.repositories.repositories_sines import SniesRepository
from app.Core.infrastructure.models.models_snies import ProgramaAcademico


class SniesRepositoryImpl(SniesRepository):

    def buscar_programas_similares(self, data):

        # -------------------------
        # 1️⃣ FILTROS FUERTES
        # -------------------------
        filtros_fuertes = Q()

        if data.get("nombre_programa"):
            filtros_fuertes |= Q(
                nombre_del_programa__icontains=data["nombre_programa"]
            )

        if data.get("campo_detallado"):
            filtros_fuertes |= Q(
                cine_f_2013_ac_campo_detallado__icontains=data["campo_detallado"]
            )

        if data.get("campo_especifico"):
            filtros_fuertes |= Q(
                cine_f_2013_ac_campo_especifico__icontains=data["campo_especifico"]
            )

        if not filtros_fuertes:
            return ProgramaAcademico.objects.none()

        # -------------------------
        # 2️⃣ PESOS
        # -------------------------
        PESOS = {
            "nombre_programa": 6,
            "campo_detallado": 5,
            "campo_especifico": 4,
        }

        # -------------------------
        # 3️⃣ QUERY BASE CON SCORE
        # -------------------------
        base_qs = (
            ProgramaAcademico.objects
            .filter(filtros_fuertes)
            .annotate(
                score=(
                    Case(
                        When(
                            nombre_del_programa__icontains=data.get("nombre_programa", ""),
                            then=Value(PESOS["nombre_programa"])
                        ),
                        default=Value(0),
                        output_field=IntegerField()
                    ) +
                    Case(
                        When(
                            cine_f_2013_ac_campo_detallado__icontains=data.get("campo_detallado", ""),
                            then=Value(PESOS["campo_detallado"])
                        ),
                        default=Value(0),
                        output_field=IntegerField()
                    ) +
                    Case(
                        When(
                            cine_f_2013_ac_campo_especifico__icontains=data.get("campo_especifico", ""),
                            then=Value(PESOS["campo_especifico"])
                        ),
                        default=Value(0),
                        output_field=IntegerField()
                    )
                )
            )
            .filter(score__gte=8)
        )

        # -------------------------
        # 4️⃣ DEDUPLICAR SIN values()
        # PostgreSQL ONLY
        # -------------------------
        qs = (
            base_qs
            .order_by(
                "nombre_del_programa",   # 👈 OBLIGATORIO primero
                "-score"                 # 👈 criterio de desempate
            )
            .distinct("nombre_del_programa")
        )[:30]

        return qs
