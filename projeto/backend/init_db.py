import sqlite3
import os

# Define os caminhos absolutos baseados na localização deste script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'database')
DB_PATH = os.path.join(DB_DIR, 'mecaeste.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

def init_database():
    """
    Inicializa o banco de dados SQLite lendo e executando o arquivo schema.sql.
    """
    # Garante que a pasta 'database' exista antes de tentar conectar
    os.makedirs(DB_DIR, exist_ok=True)
    
    # Conecta ao banco de dados (cria o arquivo se não existir)
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()
    
    try:
        # Abre e lê todo o conteúdo do arquivo SQL
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as arquivo_sql:
            script_sql = arquivo_sql.read()
            
        # Executa todos os comandos SQL de uma vez
        cursor.executescript(script_sql)
        conexao.commit()
        
        print("Sucesso: Banco de dados 'mecaeste.db' e tabelas criados com sucesso!")
        
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
        conexao.rollback()
        
    finally:
        # Garante que a conexão será fechada
        conexao.close()

if __name__ == "__main__":
    init_database()
