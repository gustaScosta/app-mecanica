import sqlite3
import os
from flask import Blueprint, jsonify

ordens_bp = Blueprint('ordens', __name__)
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'database', 'mecaeste.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@ordens_bp.route('/ordens', methods=['GET'])
def listar_ordens():
    conn = get_db_connection()
    try:
        ordens = conn.execute('''
            SELECT o.id, o.fase_atual, o.posicao_fila, o.tem_complicacao, o.criado_em,
                   v.placa, v.modelo,
                   c.nome as cliente_nome
            FROM ordens_servico o
            JOIN veiculos v ON o.veiculo_id = v.id
            JOIN clientes c ON v.cliente_id = c.id
            ORDER BY o.posicao_fila ASC
        ''').fetchall()
        return jsonify({
            'sucesso': True,
            'dados': [dict(o) for o in ordens]
        }), 200
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': f'Erro ao buscar ordens: {str(e)}'}), 500
    finally:
        conn.close()
