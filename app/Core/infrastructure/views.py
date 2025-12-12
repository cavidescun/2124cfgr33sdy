
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.Core.infrastructure.input.serializers import GenerarDocumentoSerializer, UnificacionInformacionSerializer
from app.Core.infrastructure.out.serializers import UnificarResponseSerializer
from .documentation.swagger_docs import listar_archivos_doc,email_token_doc,generar_documento_doc,unificacion_informacion_doc

from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import EmailTokenSerializer, RegistroCalificadoEntitySerializer
from app.shared.container import container

from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UnificacionInformacionView(APIView):
    
    @swagger_auto_schema(**unificacion_informacion_doc)
    def post(self, request, *args, **kwargs):
        serializer = UnificacionInformacionSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.core().unificar_informacion()
            use_case.ejecutar(serializer.validated_data["llave_maestra"])
            return Response(status=204)
        return Response(serializer.errors, status=400)
    
class GenerarInformeView(APIView):
    @swagger_auto_schema(**generar_documento_doc)
    def post(self, request, *args, **kwargs):
        serializer = GenerarDocumentoSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.core().crear_documento()
            unificar_informacion = use_case.ejecutar(serializer.data["llave_maestra"])
           # response_serializer = RegistroCalificadoEntitySerializer(unificar_informacion)
            return Response(unificar_informacion, status=200)
        return Response(serializer.errors, status=400)
        
        
class EmailTokenView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(**email_token_doc)
    def post(self, request):
        serializer = EmailTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        email = serializer.validated_data['email']
        User = get_user_model()
        user = User.objects.get(email=email)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
class DescargarInformeView(APIView):

    @swagger_auto_schema(**listar_archivos_doc)
    def get(self, request):
        llave = request.query_params.get("llave_maestra")
        file = request.query_params.get("file")
        
        descargar_informe_usecase = container.core().descargar_informe()
        if file and llave:
            try:
                ruta_archivo = descargar_informe_usecase.obtener_archivo(llave, file)
                
                if not ruta_archivo:
                    return Response({"error": "El archivo no existe"}, status=404)

                return FileResponse(
                    open(ruta_archivo, "rb"),
                    as_attachment=True,
                    filename=file,
                    content_type="application/octet-stream"
                )
            
            except ValueError as e:
                return Response({"error": str(e)}, status=404)
            
            except Exception as e:
                return Response(
                    {"error": f"Error al descargar archivo: {str(e)}"}, 
                    status=500
                )
    
        try:
            page = int(request.query_params.get("page", 1))
            page_size = int(request.query_params.get("page_size", 10))
            base_url = request.build_absolute_uri('/api/core/descargar-informe')
            
            resultado = descargar_informe_usecase.listar_archivos(
                llave=llave,
                page=page,
                page_size=page_size,
                base_url=base_url
            )
            
            return Response(resultado)
        
        except ValueError as e:
            return Response({"error": str(e)}, status=404)
        
        except Exception as e:
            return Response(
                {"error": f"Error al listar archivos: {str(e)}"}, 
                status=500
            )