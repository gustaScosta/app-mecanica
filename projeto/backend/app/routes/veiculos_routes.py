# app/routes/veiculos_routes.py - Rotas exclusivas do recurso Veículos
#
# Cada recurso da API tem seu próprio arquivo de rotas.
# Isso mantém o código organizado e fácil de manter à medida
# que o projeto cresce.

from flask import Blueprint, request, jsonify

# ----------------------------------------------------------
# Blueprint exclusivo para veículos
# ----------------------------------------------------------
veiculos_bp = Blueprint('veiculos', __name__)


@veiculos_bp.route('/veiculos', methods=['POST'])
def criar_veiculo():
    """
    POST /api/veiculos
    Recebe os dados de um veículo via JSON e retorna confirmação.

    Corpo esperado (JSON):
    {
        "placa":  "ABC-1234",
        "modelo": "Gol",
        "marca":  "Volkswagen",
        "ano":    2020
    }

    Respostas:
        201 Created     → veículo recebido com sucesso
        400 Bad Request → corpo ausente ou JSON inválido
    """
    dados = request.get_json()

    if not dados:
        return jsonify({
            'sucesso': False,
            'mensagem': 'Corpo da requisição inválido. Envie um JSON com Content-Type: application/json.'
        }), 400

    # Futuramente: validações de campos e chamada ao Controller

    return jsonify({
        'sucesso': True,
        'mensagem': 'Veículo recebido com sucesso!',
        'dados_recebidos': dados
    }), 201
