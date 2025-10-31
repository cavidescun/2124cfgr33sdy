from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from app.DocumentoMaestroPrograma.application.use_cases import DocumentMergerUseCases
from app.DocumentoMaestroPrograma.infrastructure.serializers import (
    LlaveMaestraSerializer,
)
from .docs.denominacion_programa_docs import crear_programa_doc


class DocumentoPorLlaveView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        """Vista para generar documentos."""
        serializer = LlaveMaestraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        llave_maestra = serializer.validated_data["llave_maestra"]
        casos = DocumentMergerUseCases(base_path="output")
        resultado = casos.unir_y_generar_documento_completo(llave_maestra)
        return Response(
            {
                "message": "ok",
            },
            status=status.HTTP_201_CREATED,
        )
