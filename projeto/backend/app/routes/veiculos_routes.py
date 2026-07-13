# app/routes/veiculos_routes.py - Rotas exclusivas do recurso Veículos

import sqlite3
import os
from flask import Blueprint, request, jsonify

# ----------------------------------------------------------
# Blueprint exclusivo para veículos
# ----------------------------------------------------------
veiculos_bp = Blueprint('veiculos', __name__)

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'database', 'mecaeste.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@veiculos_bp.route('/veiculos', methods=['POST'])
def criar_veiculo():
    dados = request.get_json()

    if not dados:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Corpo da requisição inválido.'
        }), 400

    placa = dados.get('placa')
    modelo = dados.get('modelo')
    marca = dados.get('marca')
    ano = dados.get('ano')

    if not all([placa, modelo, marca]):
        return jsonify({
            'sucesso': False,
            'mensagem': 'Placa, modelo e marca são obrigatórios.'
        }), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO veiculos (placa, modelo, marca, ano) VALUES (?, ?, ?, ?)',
            (placa, modelo, marca, ano)
        )
        conn.commit()
        return jsonify({
            'sucesso': True,
            'mensagem': 'Veículo salvo no banco com sucesso!',
            'dados_recebidos': dados
        }), 201
    except sqlite3.IntegrityError:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Esta placa já está cadastrada no sistema.'
        }), 409
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao salvar no banco de dados: {str(e)}'
        }), 500
    finally:
        conn.close()

@veiculos_bp.route('/veiculos', methods=['GET'])
def listar_veiculos():
    conn = get_db_connection()
    try:
        veiculos = conn.execute('''
            SELECT v.id, v.placa, v.modelo, v.marca, v.ano, c.nome as nome_cliente 
            FROM veiculos v 
            LEFT JOIN clientes c ON v.cliente_id = c.id 
            ORDER BY v.id DESC
        ''').fetchall()
        return jsonify({
            'sucesso': True,
            'dados': [dict(v) for v in veiculos]
        }), 200
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': f'Erro ao buscar veiculos: {str(e)}'}), 500
    finally:
        conn.close()
