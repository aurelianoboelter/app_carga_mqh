import oracledb
from dotenv import load_dotenv
import os
import pandas as pd

def consulta_dados():
    try:
       
        load_dotenv()

        # Credenciais do Oracle
        oracle_user = os.getenv("ORACLE_USER")
        oracle_password = os.getenv("ORACLE_PASSWORD")
        oracle_dsn = os.getenv("ORACLE_DSN")

        # Conectar ao Oracle
        oracledb.init_oracle_client(lib_dir=r"C:\Oracle\Ora12c", config_dir=r"C:\Oracle\Ora12c\Network\Admin")
        oracle_connection = oracledb.connect(
            user=oracle_user,
            password=oracle_password,
            dsn=oracle_dsn,
        )
        oracle_cursor = oracle_connection.cursor()

        # Executar consulta no Oracle
        consulta = "SELECT * FROM TD_INSTITUICAO WHERE ROWNUM <= 10"  # Limite de 10 linhas para exemplo
        oracle_cursor.execute(consulta)
        
        # Obter resultados e nomes das colunas
        resultados = oracle_cursor.fetchall()
        colunas = [desc[0] for desc in oracle_cursor.description]
        
        # Criar DataFrame para exibição
        df = pd.DataFrame(resultados, columns=colunas)
        
        # Fechar conexões
        oracle_cursor.close()
        oracle_connection.close()
        
        print("\nOperação concluída com sucesso!")
        #print(f"Retornadas {len(df)} linhas")
        print(df.head())
                  
        return df

    except (oracledb.Error, KeyError) as e:
        print(f"\nErro durante a operação: {e}")
        return pd.DataFrame()  # Retorna DataFrame vazio em caso de erro

if __name__ == "__main__":
    # Quando executado diretamente, mostra os resultados no console
    resultado = consulta_dados()
    
