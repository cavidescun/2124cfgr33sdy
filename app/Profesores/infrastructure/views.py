from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.Profesores.infrastructure.repositories import (
    ProfesoresRepositoryImpl,
)

from ..application.use_cases import CrearProfesores
from .docs.profesores_docs import crear_programa_doc
from .serializers import ProfesoresSerializer


class ProferoresView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = ProfesoresSerializer(data=request.data)
        if serializer.is_valid():
            repo = ProfesoresRepositoryImpl()
            use_case = CrearProfesores(repo)
            programa = use_case.ejectutar(**serializer.validated_data)
            return Response(
                {
                    "message": "Profesores de programa creada exitosamente",
                    "id": programa.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
