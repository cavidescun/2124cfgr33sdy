from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.AspectosCurriculares.infrastructure.repositories import (
    AspectosCurricularesRepositoryImpl,
)

from ..application.use_cases import CrearAspectosCurriculares
from .docs.aspectos_curriculares_docs import crear_programa_doc
from .serializers import AspectosCurricularesSerializer


class AspectosCurricularesView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = AspectosCurricularesSerializer(data=request.data)
        if serializer.is_valid():
            repo = AspectosCurricularesRepositoryImpl()
            use_case = CrearAspectosCurriculares(repo)
            programa = use_case.ejectutar(**serializer.validated_data)
            return Response(
                {
                    "message": "Aspectos Curriculares de programa creada exitosamente",
                    "id": programa.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
