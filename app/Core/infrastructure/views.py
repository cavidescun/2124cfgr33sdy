import shutil
import tempfile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.Core.application.use_cases import CrearLLaveMaestra
from app.Core.infrastructure.repositories import RegistroCalificadoRepositoryImpl
from .documentation.swagger_docs import crear_acta_swagger
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse, Http404
import os

class GenerarLLaveMaestraView(APIView):
    @crear_acta_swagger
    def post(self, request):
        repo = RegistroCalificadoRepositoryImpl()
        use_case = CrearLLaveMaestra(repo)
        programa = use_case.ejecutar()

        return Response(
            {"llave_id": programa.llave_documento},
            status=status.HTTP_202_ACCEPTED,
        )


class DescargarCarpetaView(APIView):
    """
    Descarga una carpeta completa desde 'output/' según la llave.
    """

    def get(self, request, llave):

        carpeta_path = os.path.join("output", llave)

        if not os.path.exists(carpeta_path):
            print("❌ Carpeta no encontrada en:", carpeta_path)  
            raise Http404("Carpeta no encontrada")

        temp_dir = tempfile.mkdtemp()
        zip_filename = f"{llave}.zip"
        zip_path = os.path.join(temp_dir, zip_filename)

        shutil.make_archive(zip_path[:-4], 'zip', carpeta_path)
        response = FileResponse(open(zip_path, "rb"), as_attachment=True)
        response["Content-Disposition"] = f'attachment; filename="{zip_filename}"'
        return response