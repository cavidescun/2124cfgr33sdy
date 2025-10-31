from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.SectorExterno.infrastructure.repositories import (
    SectorExternoRepositoryImpl,
)

from ..application.use_cases import CrearSectorExterno
from .docs.relacion_secctor_externo_docs import crear_programa_doc
from .serializers import SectorExternoSerializer


class SectorExternoView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = SectorExternoSerializer(data=request.data)
        if serializer.is_valid():
            repo = SectorExternoRepositoryImpl()
            use_case = CrearSectorExterno(repo)
            programa = use_case.ejectutar(**serializer.validated_data)
            return Response(
                {
                    "message": "Relacion con el sector externo del programa creada exitosamente",
                    "id": programa.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
