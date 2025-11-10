from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from app.Biblioteca.infrastructure.serializers import ActaQuerySerializer, FormularioPosgradoSerializer
from .docs.acta_docs import crear_acta_doc, obtener_acta_doc
from app.shared.container import container


class BibliotecaView(APIView):
    @swagger_auto_schema(**crear_acta_doc)
    def post(self, request):
        serializer = FormularioPosgradoSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.biblioteca().crear_biblioteca()  
            programa = use_case.ejecutar(**serializer.validated_data)
            return Response(
                {"message": "Justificación de programa creada exitosamente", "id": programa.id},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(query_serializer=ActaQuerySerializer, **obtener_acta_doc)
    def get(self, request):
        serializer = ActaQuerySerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        acta_id = serializer.validated_data["obtener_biblioteca_id"]
        use_case = container.biblioteca().obtener_biblioteca()
        try:
            formulario = use_case.ejecutar(acta_id)
            return Response(formulario, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
