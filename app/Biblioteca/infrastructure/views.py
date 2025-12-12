from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from app.Biblioteca.infrastructure.input.serializers import EtiquetasDinamicasSerializer,BibliotecaQuerySerializer
from app.Biblioteca.infrastructure.out.serializers import BibliotecaDetailResponseSerializer, BibliotecaResponseSerializer
from .docs.biblioteca_docs import crear_biblioteca_doc, obtener_biblioteca_doc,actualizar_biblioteca_doc
from app.shared.container import container
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.shared.auth.permissions import HasGroupPermission
class ActaPermission(HasGroupPermission):
    allowed_groups = ['admin'] 
    method_groups = {
        'POST': ['admin'],     
        'GET': ['admin', 'Editor', 'Coordinador']  
    }

class BibliotecaView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ActaPermission]
    @swagger_auto_schema(**crear_biblioteca_doc)
    def post(self, request):
        serializer = EtiquetasDinamicasSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.biblioteca().crear_biblioteca()  
            biblioteca_entity = use_case.ejecutar(**serializer.validated_data)
            response_serializer = BibliotecaResponseSerializer(biblioteca_entity)
            return Response(
                {
                    "message": "Biblioteca creada exitosamente",
                    "data": response_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(** obtener_biblioteca_doc)
    def get(self, request):
        serializer = BibliotecaQuerySerializer(data=request.GET)
        if serializer.is_valid():
            try:
                use_case = container.biblioteca().obtener_biblioteca()
                biblioteca_entity = use_case.ejecutar(**serializer.validated_data)
                response_serializer = BibliotecaDetailResponseSerializer(biblioteca_entity)
                return Response(
                    {
                        "message": "Biblioteca obtenida exitosamente",
                        "data": response_serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            


            
    @swagger_auto_schema(**actualizar_biblioteca_doc)
    def patch(self, request):

        return Response( status=status.HTTP_400_BAD_REQUEST)


                
                
