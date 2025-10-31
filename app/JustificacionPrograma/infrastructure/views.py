from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.JustificacionPrograma.infrastructure.repositories import (
    JustificacionProgramaRepositoryImpl,
)

from ..application.use_cases import CrearJustificacionPrograma
from .docs.justificacion_programa_docs import crear_programa_doc
from .serializers import JustificacionProgramaSerializer


class JustificacionProgramaView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = JustificacionProgramaSerializer(data=request.data)
        if serializer.is_valid():
            repo = JustificacionProgramaRepositoryImpl()
            use_case = CrearJustificacionPrograma(repo)
            programa = use_case.ejectutar(**serializer.validated_data)
            return Response(
                {
                    "message": "Justificacion de programa creada exitosamente",
                    "id": programa.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
