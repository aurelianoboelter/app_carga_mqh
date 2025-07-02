import oracledb
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

user = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
host = os.getenv("ORACLE_HOST")
port = os.getenv("ORACLE_PORT")
service = os.getenv("ORACLE_SERVICE")

# DSN para conexões com Oracle
dsn = f"{host}:{port}/{service}"

try:
    with oracledb.connect(user=user, password=password, dsn=dsn) as conn:
        print("✅ Conexão bem-sucedida com o Oracle!")
        cursor = conn.cursor()
        cursor.execute("SELECT SYSDATE FROM dual")
        for row in cursor:
            print("Data atual no banco:", row[0])
except Exception as e:
    print("❌ Erro na conexão com o Oracle:")
    print(e)
