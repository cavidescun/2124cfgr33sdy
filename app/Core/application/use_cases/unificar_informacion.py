from zoneinfo import ZoneInfo

from uritemplate import variables

from app.Acta.domain.repositories import ActaRepository
from app.Acuerdo.domain.repositories import AcuerdoRepository
from app.Biblioteca.domain.repositories import BibliotecaRepository
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from app.Core.domain.repositories.repositories_user import UserRepository
from app.Core.domain.repositories.repositories_sines import SniesRepository
from app.Core.domain.repositories.repositories_spadies import SpadiesRepository
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository
from app.ProyeccionTecnologica.domain.repositories import ProyeccionTecnologicaRepository
from app.shared.email.email_service import EmailService
from app.shared.email.email_template_renderer import EmailTemplateRenderer


class UnificarInformacion:
    def __init__(
        self,
        acta_repo: ActaRepository,
        biblioteca_repo: BibliotecaRepository,
        acuerdo_repo: AcuerdoRepository,
        proyeccion_fi_repo: ProyeccionFinancieraRepository,
        proyeccion_te_repo: ProyeccionInfracTecnolRepository,
        registro_repo: RegistroCalificadoRepository,
        tecnologico_repo: ProyeccionTecnologicaRepository,
        email_service: EmailService,
        template_renderer: EmailTemplateRenderer,
        repo_user: UserRepository,
        repo_snies: SniesRepository,
        repo_spadies: SpadiesRepository,
    ):
        self.acta_repo = acta_repo
        self.biblioteca_repo = biblioteca_repo
        self.acuerdo_repo = acuerdo_repo
        self.proyeccion_fi_repo = proyeccion_fi_repo
        self.proyeccion_te_repo = proyeccion_te_repo
        self.tecnologico_repo = tecnologico_repo
        self.registro_repo = registro_repo
        self.email_service = email_service
        self.template_renderer = template_renderer
        self.repo_user = repo_user
        self.repo_snies = repo_snies
        self.repo_spadies = repo_spadies

    def ejecutar(self, llave) -> dict:
        fuentes = [
            self.acta_repo.find_by_llave(llave),
            self.biblioteca_repo.find_by_llave(llave),
            self.acuerdo_repo.find_by_llave(llave),
            self.proyeccion_fi_repo.find_by_llave(llave),
            self.proyeccion_te_repo.find_by_llave(llave),
            self.tecnologico_repo.find_by_llave(llave),
        ]

        variables_unificadas = {}

        for fuente in fuentes:
            if not fuente:
                continue

            etiquetas = getattr(fuente, "etiquetas_dinamicas", None)
            if not etiquetas or not isinstance(etiquetas, dict):
                continue

            variables = (
                etiquetas
                .get("etiquetas_dinamicas", {})
                .get("variables", {})
            )

            if isinstance(variables, dict):
                variables_unificadas.update(variables)
        
        self._calcular_etiquetas_malla(variables_unificadas)
        data = {
            "etiquetas_dinamicas": {
                "variables": variables_unificadas
            }
        }

        # 🔹 Actualiza registro calificado
        registro_calificado_entity = self.registro_repo.update_by_llave(
            llave,
            data
        )

        # 🔹 Conversión y formateo de fecha (Bogotá, Colombia)
        fecha_utc = registro_calificado_entity.actualizado_en
        fecha_bogota = fecha_utc.astimezone(ZoneInfo("America/Bogota"))

        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]

        fecha_formateada = (
            f"{fecha_bogota.day} de "
            f"{meses[fecha_bogota.month - 1]} de "
            f"{fecha_bogota.year} a las "
            f"{fecha_bogota:%H:%M}"
        )

        # 🔹 Envío de correo
        emails = self.repo_user.get_all_emails()

        html_body = self.template_renderer.render(
            "unificacion.html",
            llave_maestra=llave,
            fecha_unificacion=fecha_formateada
        )

#        self.email_service.send_email(
#            to=emails,
#            subject="📄 Unificación | CUN",
#            html_body=html_body,
#        )

        return data

    def _calcular_etiquetas_malla(self, variables: dict) -> None:
        malla_curricular = variables.get("malla_curricular")
        
        if not malla_curricular or not isinstance(malla_curricular, list):
            return

        total_materias = len(malla_curricular)
        variables["total_materias"] = total_materias

        creditos_academicos_total = 0
        total_horas = 0
        creditos_disciplinares = 0
        creditos_transversal_institucional = 0
        creditos_electivos = 0

        estudios_representados = []

        estructura_componentes_area = {}

        for index, materia in enumerate(malla_curricular, start=1):
            creditos = materia.get("TR_CreditosAcademicos") or 0
            horas = materia.get("TR_Horastrabajototales") or 0
            componente = (materia.get("TE_Componente") or "").upper().strip()
            area = (materia.get("TR_Area") or "").strip()
            asignatura = (materia.get("TR_Asignatura") or "").strip()
            
            try:
                creditos = float(creditos) if creditos else 0
                horas = float(horas) if horas else 0
            except (ValueError, TypeError):
                creditos = 0
                horas = 0
            

            creditos_academicos_total += creditos

            total_horas += horas
            
            if "DISCIPLINAR" in componente:
                creditos_disciplinares += creditos
            elif "TRANSVERSAL" in componente and "INSTITUCIONAL" in componente:
                creditos_transversal_institucional += creditos
            elif "ELECTIVO" in componente:
                creditos_electivos += creditos
            
            estudio = {
                "semestre": materia.get("TR_Semestre") or "",
                "numero_orden": index,
                "asignatura": asignatura,
                "tipologia": materia.get("TR_Tipologia") or "",
                "creditosmateria": creditos,
                "horas_trabajo": horas
            }
            estudios_representados.append(estudio)
            

            componente_original = materia.get("TE_Componente") or "SIN COMPONENTE"
            
            if componente_original not in estructura_componentes_area:
                estructura_componentes_area[componente_original] = {}
            
            if area not in estructura_componentes_area[componente_original]:
                estructura_componentes_area[componente_original][area] = {
                    "asignaturas": [],
                    "creditos_totales": 0
                }
            
            estructura_componentes_area[componente_original][area]["asignaturas"].append({
                "asignatura": asignatura,
                "creditos": creditos
            })
            estructura_componentes_area[componente_original][area]["creditos_totales"] += creditos
        
        variables["creditos_academicos"] = round(creditos_academicos_total, 2)
        variables["total_horas"] = round(total_horas, 2)
        variables["creditos_disciplinares"] = round(creditos_disciplinares, 2)
        variables["creditos_transversal_institucional"] = round(creditos_transversal_institucional, 2)
        variables["creditos_electivos"] = round(creditos_electivos, 2)
        variables["estudios_representados"] = estudios_representados
        
        grafico_torta = []
        componentes = []
        
        if creditos_academicos_total > 0:
            if creditos_disciplinares > 0:
                porcentaje_disciplinar = round((creditos_disciplinares / creditos_academicos_total) * 100, 2)
                grafico_torta.append({
                    "componente": "DISCIPLINAR",
                    "creditos": creditos_disciplinares,
                    "porcentaje": porcentaje_disciplinar
                })
                componentes.append({
                    "componente": "DISCIPLINAR",
                    "porcentaje_distribucion_creditos": porcentaje_disciplinar
                })
            
            if creditos_transversal_institucional > 0:
                porcentaje_transversal = round((creditos_transversal_institucional / creditos_academicos_total) * 100, 2)
                grafico_torta.append({
                    "componente": "TRANSVERSAL-INSTITUCIONAL",
                    "creditos": creditos_transversal_institucional,
                    "porcentaje": porcentaje_transversal
                })
                componentes.append({
                    "componente": "TRANSVERSAL-INSTITUCIONAL",
                    "porcentaje_distribucion_creditos": porcentaje_transversal
                })
            
            if creditos_electivos > 0:
                porcentaje_electivos = round((creditos_electivos / creditos_academicos_total) * 100, 2)
                grafico_torta.append({
                    "componente": "ELECTIVOS",
                    "creditos": creditos_electivos,
                    "porcentaje": porcentaje_electivos
                })
                componentes.append({
                    "componente": "ELECTIVOS",
                    "porcentaje_distribucion_creditos": porcentaje_electivos
                })
        
        variables["graficodetorta_distribucion_creditos"] = grafico_torta
        variables["componentes"] = componentes

        grafico_disciplinar_vs_otros = []
        componentes_credito = []
        
        if creditos_academicos_total > 0:
            creditos_otros = creditos_transversal_institucional + creditos_electivos
            
            if creditos_disciplinares > 0:
                porcentaje_disciplinar = round((creditos_disciplinares / creditos_academicos_total) * 100, 2)
                grafico_disciplinar_vs_otros.append({
                    "componente": "DISCIPLINAR",
                    "creditos": creditos_disciplinares,
                    "porcentaje": porcentaje_disciplinar
                })
                componentes_credito.append({
                    "componente": "DISCIPLINAR",
                    "porcentaje_distribucion_componente": porcentaje_disciplinar
                })
            
            if creditos_otros > 0:
                porcentaje_otros = round((creditos_otros / creditos_academicos_total) * 100, 2)
                grafico_disciplinar_vs_otros.append({
                    "componente": "OTROS",
                    "creditos": creditos_otros,
                    "porcentaje": porcentaje_otros
                })
                componentes_credito.append({
                    "componente": "OTROS",
                    "porcentaje_distribucion_componente": porcentaje_otros
                })
        
        variables["graficodetorta_distribucion_componente"] = grafico_disciplinar_vs_otros
        variables["componentes_creditos"] = componentes_credito
        
        componentes_area = []

        creditos_por_componente = {}
        for componente, areas in estructura_componentes_area.items():
            creditos_por_componente[componente] = sum(
                area_data["creditos_totales"] for area_data in areas.values()
            )

        for componente, areas in estructura_componentes_area.items():
            creditos_componente = creditos_por_componente[componente]

            if creditos_academicos_total > 0:
                porcentaje_componente = round((creditos_componente / creditos_academicos_total) * 100, 2)
            else:
                porcentaje_componente = 0
            
            for area, area_data in areas.items():
                creditos_area = area_data["creditos_totales"]

                if creditos_componente > 0:
                    porcentaje_area = round((creditos_area / creditos_componente) * 100, 2)
                else:
                    porcentaje_area = 0
                
                for asignatura_data in area_data["asignaturas"]:
                    componentes_area.append({
                        "componente": componente,
                        "area": area,
                        "asignatura": asignatura_data["asignatura"],
                        "creditos": asignatura_data["creditos"],
                        "porcentaje_area": porcentaje_area,
                        "total_creditos": creditos_area,
                        "porcentaje_distribucion_componente": porcentaje_componente
                    })
        
        variables["componentes_area"] = componentes_area

        proporciones = []
        
        modalidad_programa = variables.get("modalidad_programa", "")
        cantidad_semanas = f"{modalidad_programa} 16 semanas" if modalidad_programa else "16 semanas"
        
        for materia in malla_curricular:
            creditos = materia.get("TR_CreditosAcademicos") or 0
            had = materia.get("TR_HorastrabajoAcom") or 0
            hti = materia.get("TR_HorastrabajoIndp") or 0
            ht = materia.get("TR_Horastrabajototales") or 0

            try:
                creditos = float(creditos) if creditos else 0
                had = float(had) if had else 0
                hti = float(hti) if hti else 0
                ht = float(ht) if ht else 0
            except (ValueError, TypeError):
                creditos = 0
                had = 0
                hti = 0
                ht = 0

            proporcion = ""
            if had > 0 and hti > 0:

                from math import gcd
                divisor = gcd(int(had), int(hti))
                ratio_had = int(had / divisor)
                ratio_hti = int(hti / divisor)
                proporcion = f"Proporción {ratio_had}:{ratio_hti}"
            elif had > 0:
                proporcion = f"Proporción {int(had)}:0"
            elif hti > 0:
                proporcion = f"Proporción 0:{int(hti)}"
            else:
                proporcion = "Proporción 0:0"
            
            proporciones.append({
                "proporcion": proporcion,
                "cantidad_semanas": cantidad_semanas,
                "creditos": creditos,
                "had": had,
                "hti": hti,
                "ht": ht
            })
        
        variables["proporciones"] = proporciones

        asignaturas = []
        
        for materia in malla_curricular:
            asignatura = materia.get("TR_Asignatura") or ""
            creditos = materia.get("TR_CreditosAcademicos") or 0
            had = materia.get("TR_HorastrabajoAcom") or 0
            hti = materia.get("TR_HorastrabajoIndp") or 0
            ht = materia.get("TR_Horastrabajototales") or 0
            semestre = materia.get("TR_Semestre") or ""
            tipologia = materia.get("TR_Tipologia") or ""

            try:
                creditos = float(creditos) if creditos else 0
                had = float(had) if had else 0
                hti = float(hti) if hti else 0
                ht = float(ht) if ht else 0
            except (ValueError, TypeError):
                creditos = 0
                had = 0
                hti = 0
                ht = 0
            
            asignaturas.append({
                "asignatura": asignatura,
                "creditos_academicos": creditos,
                "had": had,
                "hti": hti,
                "ht": ht,
                "semestre": semestre,
                "tipologia": tipologia
            })
        
        variables["asignaturas"] = asignaturas


        estadisticas_semestre = {}
        
        for materia in malla_curricular:
            semestre = str(materia.get("TR_Semestre") or "").strip()
            creditos = materia.get("TR_CreditosAcademicos") or 0

            try:
                creditos = float(creditos) if creditos else 0
            except (ValueError, TypeError):
                creditos = 0

            if semestre and semestre.upper() != "SIN SEMESTRE":
                if semestre not in estadisticas_semestre:
                    estadisticas_semestre[semestre] = {
                        "creditos": 0,
                        "asignaturas": 0
                    }
                
                estadisticas_semestre[semestre]["creditos"] += creditos
                estadisticas_semestre[semestre]["asignaturas"] += 1

        if estadisticas_semestre:
            creditos_por_semestre = [data["creditos"] for data in estadisticas_semestre.values()]
            asignaturas_por_semestre = [data["asignaturas"] for data in estadisticas_semestre.values()]
            
            min_creditos = round(min(creditos_por_semestre)) if creditos_por_semestre else 0
            max_creditos = round(max(creditos_por_semestre)) if creditos_por_semestre else 0
            
            min_asignaturas = int(min(asignaturas_por_semestre)) if asignaturas_por_semestre else 0
            max_asignaturas = int(max(asignaturas_por_semestre)) if asignaturas_por_semestre else 0
            
            variables["maxymin_espaciosacademicos"] = f"{min_creditos} y {max_creditos}"
            variables["minymax_espaciosacademicos"] = f"{min_asignaturas} y {max_asignaturas}"
        else:
            variables["maxymin_espaciosacademicos"] = "0 y 0"
            variables["minymax_espaciosacademicos"] = "0 y 0"

        tablareferentes = []
        programas_similares = variables.get("programas_similares")
        
        if programas_similares:
            nombres_programas = []
            
            if isinstance(programas_similares, str):
                nombres_programas = [
                    p.strip() 
                    for p in programas_similares.replace(';', ',').split(',')
                    if p.strip()
                ]
            elif isinstance(programas_similares, list):
                for item in programas_similares:
                    if isinstance(item, str):
                        nombres_programas.append(item.strip())
                    elif isinstance(item, dict):
                        nombre = (
                            item.get("programa") or 
                            item.get("nombre_programa") or 
                            item.get("nombre")
                        )
                        if nombre:
                            nombres_programas.append(str(nombre).strip())

            if nombres_programas:
                try:
                    programas_snies = self.repo_snies.buscar_por_nombres(nombres_programas)

                    programas_agregados = set()
                    
                    for programa in programas_snies:
                        nombre_prog = programa.nombre_del_programa
                        if nombre_prog not in programas_agregados:
                            tablareferentes.append({
                                "institucion": programa.nombre_institucion or "",
                                "programa": nombre_prog or "",
                                "modalidad": programa.modalidad or "",
                                "credito": int(programa.numero_creditos) if programa.numero_creditos else 0,
                                "periodos": int(programa.numero_periodos_de_duracion) if programa.numero_periodos_de_duracion else 0,
                                "periodicidad": programa.periodicidad or "",
                                "municipio": programa.municipio_oferta_programa or ""
                            })
                            programas_agregados.add(nombre_prog)
                except Exception:
                    pass
        
        variables["tablareferentes"] = tablareferentes

        GC_tasadesercion = []
        
        if tablareferentes and isinstance(tablareferentes, list):
            instituciones_unicas = set()
            for referente in tablareferentes:
                if isinstance(referente, dict):
                    institucion = referente.get("institucion", "").strip()
                    if institucion:
                        instituciones_unicas.add(institucion)
            for institucion in instituciones_unicas:
                try:
                    tasas = self.repo_spadies.obtener_tasas_desercion_por_institucion(institucion)
                    if tasas and tasas.get("IES"):
                        GC_tasadesercion.append(tasas)
                except Exception:
                    continue
        
        variables["GC_tasadesercion"] = GC_tasadesercion

        variables["materias_primersemestre"] = "I SEMESTRE"
    
        materias_primer_semestre = []
        for materia in malla_curricular:
            semestre = str(materia.get("TR_Semestre") or "").strip().upper()
            if semestre == "I SEMESTRE":
                asignatura = materia.get("TR_Asignatura") or ""
                if asignatura:
                    materias_primer_semestre.append(asignatura.strip())
    
        variables["listadomaterias_primersemestre"] = materias_primer_semestre
        variables["materias_segundosemestre"] = "II SEMESTRE"
    
        materias_segundo_semestre = []
        for materia in malla_curricular:
            semestre = str(materia.get("TR_Semestre") or "").strip().upper()
            if semestre == "II SEMESTRE":
                asignatura = materia.get("TR_Asignatura") or ""
                if asignatura:
                    materias_segundo_semestre.append(asignatura.strip())
    
        variables["listadomaterias_segundosemestre"] = materias_segundo_semestre

        estadisticasestudiantes = []

        if tablareferentes and isinstance(tablareferentes, list):
            instituciones_programas = []
            for referente in tablareferentes:
                if isinstance(referente, dict):
                    institucion = referente.get("institucion", "").strip()
                    programa = referente.get("programa", "").strip()
                    municipio = referente.get("municipio", "").strip()
            
                    if institucion and programa:
                        instituciones_programas.append({
                        "institucion": institucion,
                        "programa": programa,
                        "municipio": municipio
                        })
    
            if instituciones_programas:
                try:
                    estadisticasestudiantes = self.repo_snies.obtener_estadisticas_estudiantes(
                    instituciones_programas
                )
                except Exception:
                    pass

        variables["estadisticasestudiantes"] = estadisticasestudiantes

        if estadisticasestudiantes and isinstance(estadisticasestudiantes, list):
    
            inscritos_por_año = {}
            admitidos_por_año = {}
            matriculados_por_año = {}
            graduados_por_año = {}

            for estadistica in estadisticasestudiantes:
                anio = estadistica.get("anio", "") 

                try:
                    año_solo = anio.split("-")[0] if "-" in str(anio) else str(anio)
                except:
                    año_solo = str(anio)
        
                if not año_solo or año_solo == "0":
                    continue

                inscritos = estadistica.get("inscritos", 0) or 0
                admitidos = estadistica.get("admitidos", 0) or 0
                matriculados = estadistica.get("matriculados", 0) or 0
                graduados = estadistica.get("graduados", 0) or 0
        
                if año_solo not in inscritos_por_año:
                    inscritos_por_año[año_solo] = 0
                if año_solo not in admitidos_por_año:
                    admitidos_por_año[año_solo] = 0
                if año_solo not in matriculados_por_año:
                    matriculados_por_año[año_solo] = 0
                if año_solo not in graduados_por_año:
                    graduados_por_año[año_solo] = 0
        
                inscritos_por_año[año_solo] += inscritos
                admitidos_por_año[año_solo] += admitidos
                matriculados_por_año[año_solo] += matriculados
                graduados_por_año[año_solo] += graduados
    
            GC_inscritos = []
            for año in sorted(inscritos_por_año.keys(), reverse=True):
                GC_inscritos.append({
                    "años": año,
                    "inscritos": inscritos_por_año[año]
                })
    
            GC_admitidos = []
            for año in sorted(admitidos_por_año.keys(), reverse=True):
                GC_admitidos.append({
                    "años": año,
                    "admitidos": admitidos_por_año[año]
                })

            GC_matriculados = []
            for año in sorted(matriculados_por_año.keys(), reverse=True):
                GC_matriculados.append({
                    "años": año,
                    "matriculados": matriculados_por_año[año]
                })

            GC_graduados = []
            for año in sorted(graduados_por_año.keys(), reverse=True):
                GC_graduados.append({
                    "años": año,
                    "graduados": graduados_por_año[año]
                })
    

            variables["GC_inscritos"] = GC_inscritos
            variables["GC_admitidos"] = GC_admitidos
            variables["GC_matriculados"] = GC_matriculados
            variables["GC_graduados"] = GC_graduados

        else:
            variables["GC_inscritos"] = []
            variables["GC_admitidos"] = []
            variables["GC_matriculados"] = []
            variables["GC_graduados"] = []

















