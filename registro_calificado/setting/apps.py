DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_yasg",
    "django_json_widget",
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
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
