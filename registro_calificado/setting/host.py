import os


allowed_hosts = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
ALLOWED_HOSTS = [h.strip() for h in allowed_hosts if h.strip()]

DEBUG = os.getenv("DJANGO_DEBUG", "False").strip().lower() == "true"


csrf_origins_env = os.getenv("CSRF_TRUSTED_ORIGINS", "")


CSRF_TRUSTED_ORIGINS = []

for h in ALLOWED_HOSTS:
            h = h.strip()
            if h not in ("localhost", "127.0.0.1"):
                CSRF_TRUSTED_ORIGINS.append(f"https://{h}")
                CSRF_TRUSTED_ORIGINS.append(f"http://{h}")


cors_origins_env = os.getenv("CORS_ALLOWED_ORIGINS", "")

if cors_origins_env:
    CORS_ALLOWED_ORIGINS = [
        origin.strip() for origin in cors_origins_env.split(",") if origin.strip()
    ]
    CORS_ALLOW_ALL_ORIGINS = False
else:
    if DEBUG:
        CORS_ALLOW_ALL_ORIGINS = True
        CORS_ALLOWED_ORIGINS = []
    else:
        CORS_ALLOW_ALL_ORIGINS = False
        CORS_ALLOWED_ORIGINS = []
        for h in ALLOWED_HOSTS:
            h = h.strip()
            if h not in ("localhost", "127.0.0.1"):
                CORS_ALLOWED_ORIGINS.append(f"https://{h}")
                CORS_ALLOWED_ORIGINS.append(f"http://{h}")


CORS_ALLOW_CREDENTIALS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
