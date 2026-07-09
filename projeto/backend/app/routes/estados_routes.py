# app/routes/estados_routes.py - Rotas exclusivas do recurso Estados

from flask import Blueprint, request, jsonify

estados_bp = Blueprint('estados', __name__)

@estados_bp.route('/estados', methods=['POST'])
def criar_estado():
    """
    POST /api/estados
    Recebe os dados de um estado via JSON e retorna confirmação.
    """
    dados = request.get_json()

    if not dados:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Corpo da requisição inválido. Envie um JSON com Content-Type: application/json.'
        }), 400

    return jsonify({
        'sucesso': True,
        'mensagem': 'Estado recebido com sucesso!',
        'dados_recebidos': dados
    }), 201
