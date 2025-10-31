from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.InfraestructuraFisicaTecnologica.infrastructure.repositories import (
    InfraestructuraFisicaTecnologicaImpl,
)

from ..application.use_cases import CrearInfraestructuraFisicaTecnologica
from .docs.denominacion_programa_docs import crear_programa_doc
from .serializers import InfraestructuraFisicaTecnologicaSerializer


class InfraestructuraFisicaTecnologicaView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = InfraestructuraFisicaTecnologicaSerializer(data=request.data)
        if serializer.is_valid():
            repo = InfraestructuraFisicaTecnologicaImpl()
            use_case = CrearInfraestructuraFisicaTecnologica(repo)
            programa = use_case.ejecutar(**serializer.validated_data)
            return Response(
                {"message": "Programa creado exitosamente", "id": programa.id},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
