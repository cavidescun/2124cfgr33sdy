from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.InvestigacionesInnovacion.infrastructure.repositories import (
    InvestigacionesInnovacionRepositoryImpl,
)

from ..application.use_cases import CrearInvestigacionesInnovacion
from .docs.investigaciones_docs import crear_programa_doc
from .serializers import InvestigacionesInnovacionSerializer


class InvestigacionesInnovacionView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
        serializer = InvestigacionesInnovacionSerializer(data=request.data)
        if serializer.is_valid():
            repo = InvestigacionesInnovacionRepositoryImpl()
            use_case = CrearInvestigacionesInnovacion(repo)
            programa = use_case.ejectutar(**serializer.validated_data)
            return Response(
                {
                    "message": "Investestigaciones e Innovacion de programa creada exitosamente",
                    "id": programa.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
