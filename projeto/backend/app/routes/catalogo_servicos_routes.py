import sqlite3
import os
from flask import Blueprint, request, jsonify

catalogo_servicos_bp = Blueprint('catalogo_servicos', __name__)
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'database', 'mecaeste.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@catalogo_servicos_bp.route('/catalogo-servicos', methods=['GET'])
def listar_servicos():
    conn = get_db_connection()
    try:
        servicos = conn.execute('SELECT * FROM catalogo_servicos ORDER BY criado_em DESC').fetchall()
        return jsonify({
            'sucesso': True,
            'dados': [dict(s) for s in servicos]
        }), 200
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': str(e)}), 500
    finally:
        conn.close()

@catalogo_servicos_bp.route('/catalogo-servicos', methods=['POST'])
def criar_servico():
    dados = request.get_json()
    nome = dados.get('nome')
    descricao = dados.get('descricao', '')
    preco = dados.get('preco')

    if not nome or preco is None:
        return jsonify({'sucesso': False, 'mensagem': 'Nome e preco sao obrigatorios.'}), 400

    try:
        preco_float = float(preco)
    except ValueError:
        return jsonify({'sucesso': False, 'mensagem': 'Preco invalido.'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO catalogo_servicos (nome, descricao, preco) VALUES (?, ?, ?)',
            (nome, descricao, preco_float)
        )
        conn.commit()
        return jsonify({'sucesso': True, 'mensagem': 'Servico criado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': str(e)}), 500
    finally:
        conn.close()

@catalogo_servicos_bp.route('/catalogo-servicos/<id>', methods=['DELETE'])
def apagar_servico(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM catalogo_servicos WHERE id = ?', (id,))
        if cursor.rowcount == 0:
            return jsonify({'sucesso': False, 'mensagem': 'Servico nao encontrado.'}), 404
        conn.commit()
        return jsonify({'sucesso': True, 'mensagem': 'Servico apagado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': str(e)}), 500
    finally:
        conn.close()
