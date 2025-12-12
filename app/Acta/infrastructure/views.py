from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from app.Acta.infrastructure.out.serializers import ActaDetailResponseSerializer, ActaResponseSerializer, ActaUpdateResponseSerializer
from app.Acta.infrastructure.input.serializers import  ActaQuerySerializer, ActaUpdateSerializer, EtiquetasDinamicasSerializer
from .docs.acta_docs import crear_acta_doc, obtener_acta_doc,actualizar_acta_doc
from app.shared.container import container
from app.shared.auth.permissions import HasGroupPermission

class ActaPermission(HasGroupPermission):
    allowed_groups = ['admin'] 
    method_groups = {
        'POST': ['admin'],     
        'GET': ['admin', 'Editor', 'Coordinador']  
    }

class ActaView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ActaPermission]

    @swagger_auto_schema(**crear_acta_doc)
    def post(self, request):
        serializer = EtiquetasDinamicasSerializer(data=request.data)
        if serializer.is_valid():
            use_case = container.acta().crear_acta()
            acta_entity = use_case.ejecutar(**serializer.validated_data, creado_por=request.user)
            response_serializer = ActaResponseSerializer(acta_entity)
            return Response(
                {
                    "message": "Acta creada exitosamente",
                    "data": response_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(**obtener_acta_doc)
    def get(self, request):
        serializer = ActaQuerySerializer(data=request.GET)
        if serializer.is_valid():
            use_case = container.acta().obtener_acta()
            acta_entity = use_case.ejecutar(**serializer.validated_data)
            response_serializer = ActaDetailResponseSerializer(acta_entity)
            return Response(
                {
                    "message": "Acta obtenida exitosamente",
                    "data": response_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(**actualizar_acta_doc)
    def patch(self, request):
        serializer = ActaUpdateSerializer(data={ "llave_id": request.GET.get("llave_id"), "etiquetas_dinamicas": request.data.get("etiquetas_dinamicas", {})},context={"container": container})
        if  serializer.is_valid():
            validated = serializer.validated_data
            acta = validated["acta"]
            etiquetas_finales = validated["etiquetas_finales"]    
            campos_actualizados = validated["campos_actualizados"] 
            actualizar_uc = container.acta().actualizar_acta()
            actualizar_uc.ejecutar(llave_id=acta.llave_maestra,etiquetas_dinamicas=etiquetas_finales)
            response_serializer = ActaUpdateResponseSerializer({"llave_id": acta.llave_maestra,"campos_actualizados": campos_actualizados})
            return Response({
            "message": "Acta actualizada exitosamente",
            "data": response_serializer.data},
                status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
