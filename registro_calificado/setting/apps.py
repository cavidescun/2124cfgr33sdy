DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "django_json_widget",
    'rest_framework',
    'rest_framework_simplejwt',
    "corsheaders",
]

LOCAL_APPS = [
    "app.Core",
    "app.DenominacionPrograma",
    "app.JustificacionPrograma",
    "app.ActividadesAcademicas",
    "app.InfraestructuraFisicaTecnologica",
    "app.Profesores",
    "app.AspectosCurriculares",
    "app.MediosEducativos",
    "app.SectorExterno",
    "app.PresentacionDocumento",
    "app.DocumentoMaestroPrograma",
    "app.InvestigacionesInnovacion",
    "app.Acta",
    "app.Biblioteca",
    "app.IAEtiquetas",
    "app.Acuerdo",
    "app.ProyeccionInfracTecnol",
    "app.ProyeccionFinanciera",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
