import sqlite3
import os
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

clientes_bp = Blueprint('clientes', __name__)
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'database', 'mecaeste.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@clientes_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    dados = request.get_json()
    if not dados:
        return jsonify({'sucesso': False, 'mensagem': 'Corpo da requisicao invalido.'}), 400

    nome = dados.get('nome')
    idade = dados.get('idade')
    cpf = dados.get('cpf')
    email = dados.get('email')
    senha = dados.get('senha')

    if not all([nome, cpf, email, senha]):
        return jsonify({'sucesso': False, 'mensagem': 'Os campos nome, cpf, email e senha sao obrigatorios.'}), 400

    senha_hash = generate_password_hash(senha)

    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            '''INSERT INTO clientes (nome, idade, cpf, email, senha_hash) 
               VALUES (?, ?, ?, ?, ?)''',
            (nome, idade, cpf, email, senha_hash)
        )
        conn.commit()
        return jsonify({'sucesso': True, 'mensagem': 'Cliente cadastrado com sucesso!'}), 201
    except sqlite3.IntegrityError as e:
        # Identifica o erro real em vez de retornar sempre a mesma mensagem
        msg = str(e)
        if 'cpf' in msg.lower() or 'UNIQUE' in msg:
            return jsonify({'sucesso': False, 'mensagem': 'O CPF informado ja esta cadastrado.'}), 409
        return jsonify({'sucesso': False, 'mensagem': f'Erro de integridade: {msg}'}), 409
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': f'Erro ao salvar cliente: {str(e)}'}), 500
    finally:
        conn.close()

@clientes_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = get_db_connection()
    try:
        # Retorna todos os clientes exceto o hash da senha
        clientes = conn.execute('SELECT id, nome, idade, cpf, email, telefone, criado_em FROM clientes ORDER BY criado_em DESC').fetchall()
        return jsonify({
            'sucesso': True,
            'dados': [dict(c) for c in clientes]
        }), 200
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': f'Erro ao buscar clientes: {str(e)}'}), 500
    finally:
        conn.close()
