#!/bin/bash
set -e

echo "=== 🚀 Iniciando entorno local de desarrollo ==="

echo "⌛ Esperando a que las bases de datos estén listas..."

# Esperar a PostgreSQL
echo "📊 Verificando PostgreSQL..."
until python -c "import psycopg2; psycopg2.connect(host='${POSTGRES_HOST}', user='${POSTGRES_USER}', password='${POSTGRES_PASSWORD}', dbname='${POSTGRES_DB}')" &> /dev/null; do
  echo "⏳ PostgreSQL no está listo - esperando..."
  sleep 2
done
echo "✅ PostgreSQL está listo"

# Esperar a SQL Server (conectando como SA, que SIEMPRE existe)
echo "📊 Verificando SQL Server..."


# AHORA sí, inicializar la base de datos (siempre con SA)
echo "🔧 Inicializando base de datos SQL Server..."
python << 'PYEND'
import pyodbc
import os

server = os.getenv('SQLSERVER_HOST')
sa_password = os.getenv('SQLSERVER_PASSWORD')
database = os.getenv('SQLSERVER_DB')
user = os.getenv('SQLSERVER_USER')
user_password = 'Cun2024*'

try:
    # SIEMPRE conectamos como SA
    print(f"🔌 Conectando a SQL Server como SA...")
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'UID=sa;'
        f'PWD={sa_password};'
        f'TrustServerCertificate=yes',
        timeout=30
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # 1. Verificar/Crear base de datos
    cursor.execute(f"SELECT database_id FROM sys.databases WHERE name = '{database}'")
    if not cursor.fetchone():
        print(f"📦 Creando base de datos '{database}'...")
        cursor.execute(f"CREATE DATABASE [{database}]")
        print(f"✅ Base de datos '{database}' creada")
    else:
        print(f"ℹ️  Base de datos '{database}' ya existe")
    
    # 2. Verificar/Crear login
    cursor.execute(f"SELECT name FROM sys.server_principals WHERE name = '{user}'")
    if not cursor.fetchone():
        print(f"👤 Creando login '{user}'...")
        cursor.execute(f"CREATE LOGIN [{user}] WITH PASSWORD = '{user_password}'")
        print(f"✅ Login '{user}' creado")
    else:
        print(f"ℹ️  Login '{user}' ya existe")
    
    # 3. Cambiar a la base de datos
    cursor.execute(f"USE [{database}]")
    
    # 4. Verificar/Crear usuario en la base de datos
    cursor.execute(f"SELECT name FROM sys.database_principals WHERE name = '{user}'")
    if not cursor.fetchone():
        print(f"👤 Creando usuario '{user}' en la base de datos...")
        cursor.execute(f"CREATE USER [{user}] FOR LOGIN [{user}]")
        cursor.execute(f"ALTER ROLE db_owner ADD MEMBER [{user}]")
        print(f"✅ Usuario '{user}' creado con permisos de propietario")
    else:
        print(f"ℹ️  Usuario '{user}' ya existe en la base de datos")
        # Asegurar que tenga permisos (por si acaso)
        cursor.execute(f"ALTER ROLE db_owner ADD MEMBER [{user}]")
    
    cursor.close()
    conn.close()
    print("✅ SQL Server inicializado correctamente")
    
except Exception as e:
    print(f"❌ Error inicializando SQL Server: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
PYEND

echo "📦 Aplicando migraciones..."
python manage.py migrate --noinput

echo "👤 Verificando superusuario..."
python manage.py shell << 'END'
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f"✅ Superusuario '{username}' creado.")
else:
    print(f"ℹ️ El superusuario '{username}' ya existe.")
END

echo "✅ Todo listo. Iniciando servidor de desarrollo..."
exec "$@"