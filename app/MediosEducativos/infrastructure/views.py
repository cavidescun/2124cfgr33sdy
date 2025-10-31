from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.MediosEducativos.infrastructure.repositories import (
    MediosEducativosRepositoryImpl,
)

from ..application.use_cases import CrearMediosEducativos
from .docs.medios_educativos_docs import crear_programa_doc
from .serializers import MediosEducativosSerializer


class MediosEducativosView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = MediosEducativosSerializer(data=request.data)
        if serializer.is_valid():
            repo = MediosEducativosRepositoryImpl()
            use_case = CrearMediosEducativos(repo)
            programa = use_case.ejectutar(**serializer.validated_data)
            return Response(
                {
                    "message": "Medios educativos para el programa creada exitosamente",
                    "id": programa.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
