from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from app.Acuerdo.infrastructure.input.serializers import EtiquetasDinamicasSerializer, AcuerdoQuerySerializer
from app.Acuerdo.infrastructure.out.serializers import AcuerdoDetailResponseSerializer, AcuerdoResponseSerializer
from .docs.acuerdo_docs import crear_acuerdo_doc, obtener_acuerdo_doc,actualizar_acuerdo_doc
from app.shared.container import container
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.shared.auth.permissions import HasGroupPermission

class AcuerdoPermission(HasGroupPermission):
    allowed_groups = ['admin']
    method_groups = {
        'POST':['admin'],
        'GET':['admin','editor','coordinador']
    }

class AcuerdoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AcuerdoPermission]

    @swagger_auto_schema(**crear_acuerdo_doc)
    def post(self, request):
        serializer = EtiquetasDinamicasSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.acuerdo().crear_acuerdo()
            acuerdo_entity = use_case.ejecutar(**serializer.validated_data)
            response_serializer = AcuerdoResponseSerializer(acuerdo_entity)
            return Response(
                {
                "message":"Acuerdo creado exitosamente",
                "data": response_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(**obtener_acuerdo_doc)
    def get(self, request):
        serializer = AcuerdoQuerySerializer(data=request.GET)
        if serializer.is_valid():
            try:
                use_case = container.acuerdo().obtener_acuerdo()
                acuerdo_entity = use_case.ejecutar(**serializer.validated_data)
                response_serializer = AcuerdoDetailResponseSerializer(acuerdo_entity)
                return Response(
                    {
                        "message":"Acuerdo obtenido exitosamente",
                        "data": response_serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(**actualizar_acuerdo_doc)
    def patch(self, request):

        return Response( status=status.HTTP_400_BAD_REQUEST)

