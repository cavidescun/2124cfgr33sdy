from urllib import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
import json
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from app.Acuerdo.infrastructure.input.serializers import AcuerdoUpdateSerializer, EtiquetasDinamicasSerializer, AcuerdoQuerySerializer
from app.Acuerdo.infrastructure.out.serializers import AccuerdoUpdateResponseSerializer, AcuerdoDetailResponseSerializer, AcuerdoResponseSerializer
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
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    @swagger_auto_schema(**crear_acuerdo_doc)
    def post(self, request):
        if request.content_type and 'multipart/form-data' in request.content_type:
            data = dict(request.data)

        for key in data:
            if isinstance(data[key], list) and len(data[key]) == 1:
                data[key] = data[key][0]

        if 'etiquetas_dinamicas' in data and isinstance(data['etiquetas_dinamicas'], str):
            try:
                data['etiquetas_dinamicas'] = json.loads(data['etiquetas_dinamicas'])
            except json.JSONDecodeError:
                return Response(
                    {"error": "El campo 'etiquetas_dinamicas' no es un JSON válido."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            data = request.data
    
        serializer = EtiquetasDinamicasSerializer(data=data)
    
        if serializer.is_valid():
            validated_data = serializer.validated_data.copy()
        
            validated_data.pop('archivo_excel', None)
        
       
            use_case = container.acuerdo().crear_acuerdo()
            acuerdo_entity = use_case.ejecutar(**validated_data, creado_por=request.user)
            response_serializer = AcuerdoResponseSerializer(acuerdo_entity)
            return Response(
            {
                "message": "Acuerdo creado exitosamente",
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
        serializer = AcuerdoUpdateSerializer(data={ "llave_id": request.GET.get("llave_id"), "etiquetas_dinamicas": request.data.get("etiquetas_dinamicas", {})},context={"container": container})
        if  serializer.is_valid():
            validated = serializer.validated_data
            proyeccion = validated["acuerdo"]
            etiquetas_finales = validated["etiquetas_finales"]    
            campos_actualizados = validated["campos_actualizados"] 
            actualizar_uc = container.acuerdo().actualizar_acuerdo()
            actualizar_uc.ejecutar(llave_id=proyeccion.llave_maestra,etiquetas_dinamicas=etiquetas_finales,user=request.user)
            response_serializer = AccuerdoUpdateResponseSerializer({"llave_id": proyeccion.llave_maestra,"campos_actualizados": campos_actualizados})
            return Response({
            "message": "Proyeccion Acuerdo actualizada exitosamente",
            "data": response_serializer.data},
                status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

