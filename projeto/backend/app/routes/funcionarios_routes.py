# app/routes/funcionarios_routes.py - Rotas exclusivas do recurso Funcionários

from flask import Blueprint, request, jsonify

funcionarios_bp = Blueprint('funcionarios', __name__)

@funcionarios_bp.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    """
    POST /api/funcionarios
    Recebe os dados de um funcionário via JSON e retorna confirmação.
    """
    dados = request.get_json()

    if not dados:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Corpo da requisição inválido. Envie um JSON com Content-Type: application/json.'
        }), 400

    return jsonify({
        'sucesso': True,
        'mensagem': 'Funcionário recebido com sucesso!',
        'dados_recebidos': dados
    }), 201
