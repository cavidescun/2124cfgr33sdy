from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    AnalizarIARequestSerializer,
    AnalizarIAResponseSerializer,
    PromptTemplateSerializer,
    PromptTemplateCreateRequestSerializer
)
from .docs.analisis_ia_docs import (
    analizar_ia_doc, 
    listar_templates_doc,
    crear_template_doc,
    obtener_template_doc,
    eliminar_template_doc,
    crear_multiples_templates_doc
)
from .repositories import AnalisisIARepositoryImpl, PromptTemplateRepositoryImpl
from .services.openai_services import OpenAIService
from ..application.use_cases import (
    AnalizarConIA, 
    CrearTemplate,
    ObtenerTemplate,
    ListarTemplates,
    EliminarTemplate
)

class AnalizarIAView(APIView):   
    @swagger_auto_schema(**analizar_ia_doc)
    def post(self, request):
        serializer = AnalizarIARequestSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            nombre_etiqueta = serializer.validated_data['nombre_etiqueta']
            datos = serializer.validated_data['datos']
            prompt_custom = serializer.validated_data.get('prompt_custom')
            ia_service = OpenAIService()
            analisis_repo = AnalisisIARepositoryImpl()
            template_repo = PromptTemplateRepositoryImpl()
            use_case = AnalizarConIA(ia_service, analisis_repo, template_repo)
            resultado = use_case.ejecutar(nombre_etiqueta, datos, prompt_custom)
            response_serializer = AnalizarIAResponseSerializer(resultado)
            
            return Response(
                {
                    "message": "Análisis completado exitosamente",
                    "data": response_serializer.data
                },
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except RuntimeError as e:
            return Response(
                {"error": f"Error al procesar con IA: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": f"Error inesperado: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PromptTemplatesView(APIView): 
    @swagger_auto_schema(**listar_templates_doc)
    def get(self, request):
        try:
            template_repo = PromptTemplateRepositoryImpl()
            use_case = ListarTemplates(template_repo)
            templates = use_case.ejecutar()
            
            serializer = PromptTemplateSerializer(
                [
                    {
                        'nombre_etiqueta': t.nombre_etiqueta,
                        'prompt_template': t.prompt_template,
                        'descripcion': t.descripcion
                    }
                    for t in templates
                ],
                many=True
            )
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"Error al obtener templates: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @swagger_auto_schema(**crear_template_doc)
    def post(self, request):
        serializer = PromptTemplateSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            template_repo = PromptTemplateRepositoryImpl()
            use_case = CrearTemplate(template_repo)
            
            template = use_case.ejecutar(
                nombre_etiqueta=serializer.validated_data['nombre_etiqueta'],
                prompt_template=serializer.validated_data['prompt_template'],
                descripcion=serializer.validated_data.get('descripcion')
            )
            
            response_serializer = PromptTemplateSerializer({
                'nombre_etiqueta': template.nombre_etiqueta,
                'prompt_template': template.prompt_template,
                'descripcion': template.descripcion
            })
            
            return Response(
                {
                    "message": "Template creado/actualizado exitosamente",
                    "data": response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
            
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": f"Error al crear template: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PromptTemplateDetailView(APIView):  
    @swagger_auto_schema(**obtener_template_doc)
    def get(self, request, nombre_etiqueta):
        try:
            template_repo = PromptTemplateRepositoryImpl()
            use_case = ObtenerTemplate(template_repo)
            
            template = use_case.ejecutar(nombre_etiqueta)
            
            if not template:
                return Response(
                    {"error": f"Template '{nombre_etiqueta}' no encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = PromptTemplateSerializer({
                'nombre_etiqueta': template.nombre_etiqueta,
                'prompt_template': template.prompt_template,
                'descripcion': template.descripcion
            })
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"error": f"Error al obtener template: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @swagger_auto_schema(**eliminar_template_doc)
    def delete(self, request, nombre_etiqueta):
        """Elimina (desactiva) un template"""
        try:
            template_repo = PromptTemplateRepositoryImpl()
            use_case = EliminarTemplate(template_repo)
            
            eliminado = use_case.ejecutar(nombre_etiqueta)
            
            if not eliminado:
                return Response(
                    {"error": f"Template '{nombre_etiqueta}' no encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            return Response(
                {"message": f"Template '{nombre_etiqueta}' eliminado exitosamente"},
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            return Response(
                {"error": f"Error al eliminar template: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PromptTemplatesBatchView(APIView):    
    @swagger_auto_schema(**crear_multiples_templates_doc)
    def post(self, request):
        serializer = PromptTemplateCreateRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            template_repo = PromptTemplateRepositoryImpl()
            use_case = CrearTemplate(template_repo)
            
            templates_creados = []
            
            for template_data in serializer.validated_data['templates']:
                template = use_case.ejecutar(
                    nombre_etiqueta=template_data['nombre_etiqueta'],
                    prompt_template=template_data['prompt_template'],
                    descripcion=template_data.get('descripcion')
                )
                templates_creados.append({
                    'nombre_etiqueta': template.nombre_etiqueta,
                    'prompt_template': template.prompt_template,
                    'descripcion': template.descripcion
                })
            
            return Response(
                {
                    "message": f"{len(templates_creados)} templates creados/actualizados exitosamente",
                    "created": len(templates_creados),
                    "templates": templates_creados
                },
                status=status.HTTP_201_CREATED
            )
            
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": f"Error al crear templates: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )