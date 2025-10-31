
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from app.Acta.infrastructure.serializers import FormularioPosgradoSerializer
from .docs.actividades_academicas_docs import crear_programa_doc
from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from ..application.use_cases import CrearActa
class ActaView(APIView):
    @swagger_auto_schema(**crear_programa_doc)
    def post(self, request):
            print(request.data)
            serializer = FormularioPosgradoSerializer(data=request.data)
            if serializer.is_valid():
                repo = ActaRepositoryImpl()
                use_case = CrearActa(repo)
                programa = use_case.ejectutar(**serializer.validated_data)
                return Response(
                    {
                        "message": "Justificacion de programa creada exitosamente",
                        "id": programa.id,
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

