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
    },

    "sqlserver_db1": {
                "ENGINE": "mssql",
                "NAME": os.getenv("SQLSERVER_DB"),
                "USER": os.getenv("SQLSERVER_USER"),
                "PASSWORD": os.getenv("SQLSERVER_PASSWORD"),
                "HOST": os.getenv("SQLSERVER_HOST"),
                "PORT": os.getenv("SQLSERVER_PORT", "1433"),
                "OPTIONS": {
                    "driver": "ODBC Driver 17 for SQL Server",
                },
            },

    "sqlserver_db2": {
                "ENGINE": "mssql",
                "NAME": os.getenv("SQLSERVER_DB2"),
                "USER": os.getenv("SQLSERVER_USER"),
                "PASSWORD": os.getenv("SQLSERVER_PASSWORD"),
                "HOST": os.getenv("SQLSERVER_HOST"),
                "PORT": os.getenv("SQLSERVER_PORT", "1433"),
                "OPTIONS": {
                    "driver": "ODBC Driver 17 for SQL Server",
        },
    },


}

DATABASE_ROUTERS = ["app.Core.infrastructure.db_router.SQLServerRouter"]
