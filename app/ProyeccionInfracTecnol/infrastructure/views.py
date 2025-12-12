from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from app.ProyeccionInfracTecnol.infrastructure.input.serializers import EtiquetasDinamicasSerializer, ProyeccionInfracTecnolQuerySerializer
from app.ProyeccionInfracTecnol.infrastructure.out.serializers import ProyeccionInfracTecnolResponseSerializer, ProyeccionInfracTecnolDetailResponseSerializer
from .docs.proyeccionInfraTecnol_docs import crear_proyeccion_infrac_tecnol_doc, obtener_proyeccion_infrac_tecnol_doc,actualizar_proyeccion_infrac_tecnol_doc
from app.shared.container import container
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.shared.auth.permissions import HasGroupPermission

class ProyeccionInfracTecnolPermission(HasGroupPermission):
    allowed_groups = ['admin']
    method_groups = {
        'POST':['admin'],
        'GET':['admin','editor','coordinador']
    }

class ProyeccionInfracTecnolView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ProyeccionInfracTecnolPermission]

    @swagger_auto_schema(**crear_proyeccion_infrac_tecnol_doc)
    def post(self, request):
        serializer = EtiquetasDinamicasSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.proyeccion_infrac_tecnol().crear_proyeccion_infrac_tecnol()
            proyeccion_entity = use_case.ejecutar(**serializer.validated_data)
            response_serializer = ProyeccionInfracTecnolResponseSerializer(proyeccion_entity)
            return Response(
                {
                "message":"Proyección de infraestructura tecnológica creada exitosamente",
                "data": response_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(**obtener_proyeccion_infrac_tecnol_doc)
    def get(self, request):
        serializer = ProyeccionInfracTecnolQuerySerializer(data=request.GET)
        if serializer.is_valid():
            try:
                use_case = container.proyeccion_infrac_tecnol().obtener_proyeccion_infrac_tecnol()
                proyeccion_entity = use_case.ejecutar(**serializer.validated_data)
                response_serializer = ProyeccionInfracTecnolDetailResponseSerializer(proyeccion_entity)
                return Response(
                    {
                        "message":"Proyección de infraestructura tecnológica obtenida exitosamente",
                        "data": response_serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**actualizar_proyeccion_infrac_tecnol_doc)
    def patch(self, request):

        return Response( status=status.HTTP_400_BAD_REQUEST)
