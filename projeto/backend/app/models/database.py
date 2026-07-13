import sqlite3
import os

# Define os caminhos absolutos para o banco de dados e o arquivo SQL
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'sistema_mecanico.db')
SCHEMA_PATH = os.path.join(BASE_DIR, '..', 'schema.sql')

def get_db_connection():
    """
    Cria e retorna uma conexão com o banco de dados SQLite.
    No Python, utilizamos a biblioteca nativa 'sqlite3', que tem o papel equivalente 
    ao do PDO (PHP Data Objects) no ecossistema PHP.
    """
    conn = sqlite3.connect(DB_PATH)
    
    # row_factory permite acessar as colunas pelo nome (ex: row['Nome']), similar ao PDO::FETCH_ASSOC do PHP
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    """
    Lê o arquivo schema.sql e executa as queries para criar as tabelas no banco de dados.
    """
    conn = get_db_connection()
    try:
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        print("Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    # Se você rodar este arquivo isoladamente, ele irá criar o banco de dados.
    init_db()
