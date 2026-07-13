# app/routes/servicos_prestados_routes.py - Rotas exclusivas do recurso Serviços Prestados

from flask import Blueprint, request, jsonify

servicos_prestados_bp = Blueprint('servicos_prestados', __name__)

@servicos_prestados_bp.route('/servicos-prestados', methods=['POST'])
def criar_servico_prestado():
    """
    POST /api/servicos-prestados
    Recebe os dados de um serviço prestado via JSON e retorna confirmação.
    """
    dados = request.get_json()

    if not dados:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Corpo da requisição inválido. Envie um JSON com Content-Type: application/json.'
        }), 400

    return jsonify({
        'sucesso': True,
        'mensagem': 'Serviço Prestado recebido com sucesso!',
        'dados_recebidos': dados
    }), 201
