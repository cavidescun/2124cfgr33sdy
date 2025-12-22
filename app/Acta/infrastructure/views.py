from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from app.Acta.infrastructure.out.serializers import ActaAprobacionResponseSerializer, ActaDetailResponseSerializer, ActaResponseSerializer, ActaUpdateResponseSerializer
from app.Acta.infrastructure.input.serializers import  ActaAprobacionSerializer, ActaQuerySerializer, ActaUpdateSerializer, EtiquetasDinamicasSerializer
from .docs.acta_docs import crear_acta_doc, obtener_acta_doc,actualizar_acta_doc,acta_aprobacion_doc
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
            actualizar_uc.ejecutar(llave_id=acta.llave_maestra,etiquetas_dinamicas=etiquetas_finales,user=request.user)
            response_serializer = ActaUpdateResponseSerializer({"llave_id": acta.llave_maestra,"campos_actualizados": campos_actualizados})
            return Response({
            "message": "Acta actualizada exitosamente",
            "data": response_serializer.data},
                status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**acta_aprobacion_doc)
    def put(self, request):
        serializer = ActaAprobacionSerializer(
            data={
                "llave_id": request.query_params.get("llave_id"),
                "flag": request.data.get("flag"),
            }
        )

        if serializer.is_valid():
            validated = serializer.validated_data

            use_case = container.acta().aprobar_acta()
            use_case.ejecutar(
                llave_id=validated["llave_id"],
                aprobado=validated["flag"],
                usuario=request.user  
            )

            response_serializer = ActaAprobacionResponseSerializer({
                "llave_id": validated["llave_id"],
                "aprobado": validated["flag"]
            })

            return Response(
                {
                    "message": "Estado del acta actualizado correctamente",
                    "data": response_serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
