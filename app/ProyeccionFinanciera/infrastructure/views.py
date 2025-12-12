from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from app.ProyeccionFinanciera.infrastructure.input.serializers import EtiquetasDinamicasSerializer, ProyeccionFinancieraQuerySerializer
from app.ProyeccionFinanciera.infrastructure.out.serializers import ProyeccionFinancieraDetailResponseSerializer, ProyeccionFinancieraDetailResponseSerializer, ProyeccionFinancieraResponseSerializer
from .docs.proyeccionFinanciera_docs import crear_proyeccionFinanciera_doc, obtener_proyeccionFinanciera_doc,actualizar_proyeccionFinanciera_doc
from app.shared.container import container
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.shared.auth.permissions import HasGroupPermission

class ProyeccionFinancieraPermission(HasGroupPermission):
    allowed_groups = ['admin']
    method_groups = {
        'POST':['admin'],
        'GET':['admin','editor','coordinador']
    }

class ProyeccionFinancieraView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ProyeccionFinancieraPermission]

    @swagger_auto_schema(**crear_proyeccionFinanciera_doc)
    def post(self, request):
        serializer = EtiquetasDinamicasSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.proyeccion_financiera().crear_proyeccionFinanciera()
            proyeccion_entity = use_case.ejecutar(**serializer.validated_data)
            response_serializer = ProyeccionFinancieraResponseSerializer(proyeccion_entity)
            return Response(
                {
                "message":"Proyección financiera creada exitosamente",
                "data": response_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(**obtener_proyeccionFinanciera_doc)
    def get(self, request):
        serializer = ProyeccionFinancieraQuerySerializer(data=request.GET)
        if serializer.is_valid():
            try:
                use_case = container.proyeccion_financiera().obtener_proyeccionFinanciera()
                proyeccion_entity = use_case.ejecutar(**serializer.validated_data)
                response_serializer = ProyeccionFinancieraDetailResponseSerializer(proyeccion_entity)
                return Response(
                    {
                        "message":"Proyección financiera obtenida exitosamente",
                        "data": response_serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**actualizar_proyeccionFinanciera_doc)
    def patch(self, request):

        return Response( status=status.HTTP_400_BAD_REQUEST)

