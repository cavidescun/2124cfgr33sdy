import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": "5432",
        "OPTIONS": {
            "options": f"-c search_path={os.getenv('POSTGRES_SCHEMA', 'public')},public",
        },
    },

    "snies": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": "5432",
        "OPTIONS": {
            "options": "-c search_path=SNIES,public",
        },
    }
}

DATABASE_ROUTERS = ["app.Core.infrastructure.db_router.SQLServerRouter"]
