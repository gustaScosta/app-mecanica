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
    # Garante que o corpo da requisicao e um JSON valido
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({'sucesso': False, 'mensagem': 'Corpo da requisicao invalido. Envie um JSON com Content-Type: application/json.'}), 400

    nome = dados.get('nome', '').strip()
    descricao = dados.get('descricao', '').strip()
    preco = dados.get('preco')

    # Validacao dos campos obrigatorios
    if not nome:
        return jsonify({'sucesso': False, 'mensagem': 'O campo "nome" e obrigatorio.'}), 400

    if preco is None or preco == '':
        return jsonify({'sucesso': False, 'mensagem': 'O campo "preco" e obrigatorio.'}), 400

    # Converte preco para float, capturando tanto ValueError quanto TypeError
    try:
        preco_float = float(preco)
        if preco_float < 0:
            return jsonify({'sucesso': False, 'mensagem': 'O preco nao pode ser negativo.'}), 400
    except (ValueError, TypeError):
        return jsonify({'sucesso': False, 'mensagem': 'Valor de preco invalido. Use um numero (ex: 50.00).'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO catalogo_servicos (nome, descricao, preco) VALUES (?, ?, ?)',
            (nome, descricao, preco_float)
        )
        conn.commit()
        novo_id = cursor.lastrowid
        return jsonify({
            'sucesso': True,
            'mensagem': 'Servico criado com sucesso!',
            'id': novo_id
        }), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'sucesso': False, 'mensagem': f'Erro ao salvar no banco de dados: {str(e)}'}), 500
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
        conn.rollback()
        return jsonify({'sucesso': False, 'mensagem': str(e)}), 500
    finally:
        conn.close()
