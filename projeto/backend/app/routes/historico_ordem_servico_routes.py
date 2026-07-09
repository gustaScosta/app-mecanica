# app/routes/historico_ordem_servico_routes.py - Rotas exclusivas do recurso Histórico de Ordem de Serviço

from flask import Blueprint, request, jsonify

historico_ordem_servico_bp = Blueprint('historico_ordem_servico', __name__)

@historico_ordem_servico_bp.route('/historico-ordem-servico', methods=['POST'])
def criar_historico_ordem_servico():
    """
    POST /api/historico-ordem-servico
    Recebe os dados de um histórico de ordem de serviço via JSON e retorna confirmação.
    """
    dados = request.get_json()

    if not dados:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Corpo da requisição inválido. Envie um JSON com Content-Type: application/json.'
        }), 400

    return jsonify({
        'sucesso': True,
        'mensagem': 'Histórico de Ordem de Serviço recebido com sucesso!',
        'dados_recebidos': dados
    }), 201
