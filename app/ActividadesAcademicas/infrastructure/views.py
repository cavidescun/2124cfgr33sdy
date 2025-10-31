from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.ActividadesAcademicas.infrastructure.repositories import (
    ActividadesAcademicasRepositoryImpl,
)

from ..application.use_cases import CrearActividadesAcademicas
from .docs.actividades_academicas_docs import crear_programa_doc
from .serializers import ActividadesAcademicasSerializer


class ActividadesAcademicasView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = ActividadesAcademicasSerializer(data=request.data)
        if serializer.is_valid():
            repo = ActividadesAcademicasRepositoryImpl()
            use_case = CrearActividadesAcademicas(repo)
            programa = use_case.ejectutar(**serializer.validated_data)
            return Response(
                {
                    "message": "Justificacion de programa creada exitosamente",
                    "id": programa.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
