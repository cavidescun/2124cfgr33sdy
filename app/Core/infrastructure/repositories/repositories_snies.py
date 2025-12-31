from django.db.models import (
    Q, Case, When, IntegerField, Value, Max, F
)
from app.Core.domain.repositories.repositories_sines import SniesRepository
from app.Core.infrastructure.models.models_snies import ProgramaAcademico, ConsolidadoEducacionSuperior
from typing import List, Dict, Any


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

    def buscar_por_nombres(self, nombres_programas: List[str]) -> List:
        if not nombres_programas:
            return []
        
        resultados = []
        programas_encontrados = set()
        
        for nombre in nombres_programas:
            if not nombre or not nombre.strip():
                continue
            
            # ✅ Agregar filtro de estado_programa = 'Activo'
            programa = ProgramaAcademico.objects.filter(
                nombre_del_programa__icontains=nombre.strip(),
                estado_programa__iexact='Activo'  # ✅ NUEVO FILTRO
            ).first()
            
            if programa and programa.nombre_del_programa not in programas_encontrados:
                resultados.append(programa)
                programas_encontrados.add(programa.nombre_del_programa)
        
        return resultados

    def obtener_estadisticas_estudiantes(self, instituciones_programas: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """
        Obtiene estadísticas de estudiantes para TODAS las instituciones y programas
        ✅ CAMBIO 2: Agregar semestre al año y validar municipio
        """
        if not instituciones_programas:
            return []
        
        resultados = []
        
        for item in instituciones_programas:
            institucion = item.get("institucion", "").strip()
            programa = item.get("programa", "").strip()
            municipio = item.get("municipio", "").strip()  # ✅ NUEVO: obtener municipio
            
            if not institucion or not programa:
                continue
            
            try:
                # ✅ Construir filtro con municipio si existe
                filtros = Q(
                    institucion__icontains=institucion,
                    programa_academico__icontains=programa
                )
                
                # ✅ NUEVO: Agregar filtro de municipio si está presente
                if municipio:
                    filtros &= Q(municipio_programa__icontains=municipio)
                
                registros = ConsolidadoEducacionSuperior.objects.filter(
                    filtros
                ).order_by('-anio', '-semestre')
                
                for registro in registros:
                    # ✅ NUEVO: Combinar año y semestre
                    anio_semestre = f"{registro.anio or 0}-{registro.semestre or 0}"
                    
                    resultados.append({
                        "institucion_educacion_superior": registro.institucion or "",
                        "programa_academico": registro.programa_academico or "",
                        "anio": anio_semestre,  # ✅ CAMBIADO: ahora incluye semestre
                        "inscritos": registro.total_inscritos or 0,
                        "admitidos": registro.total_admitidos or 0,
                        "graduados": registro.total_graduados or 0,
                        "matriculados": registro.total_matriculados or 0
                    })
                
            except Exception as e:
                print(f"❌ Error buscando: {institucion} - {programa}: {str(e)}")
                continue
        
        return resultados




