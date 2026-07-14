# run.py - Entrypoint (Arquivo Principal) do Servidor Flask
#
# E aqui que a aplicacao "nasce". Toda configuracao global,
# registro de Blueprints (grupos de rotas) e inicializacao
# do servidor acontecem neste arquivo.

from flask import Flask
from flask_cors import CORS
from app.routes.veiculos_routes import veiculos_bp
from app.routes.funcionarios_routes import funcionarios_bp
from app.routes.estados_routes import estados_bp
from app.routes.servicos_prestados_routes import servicos_prestados_bp
from app.routes.historico_ordem_servico_routes import historico_ordem_servico_bp
from app.routes.clientes_routes import clientes_bp
from app.routes.catalogo_servicos_routes import catalogo_servicos_bp
from app.routes.ordens_routes import ordens_bp
from init_db import init_database

def create_app():
    """
    Fabrica da aplicacao Flask (padrao Application Factory).

    Em vez de criar o 'app' diretamente no escopo global,
    usamos uma funcao para cria-lo. Isso torna o codigo
    mais testavel, flexivel e escalavel.

    Returns:
        Flask: instancia configurada da aplicacao.
    """
    # Garante que o banco de dados e todas as tabelas existam antes de iniciar
    init_database()

    app = Flask(__name__)

    # Ativa o CORS para permitir requisicoes do frontend (HTML/JS)
    CORS(app)

    # ----------------------------------------------------------
    # Registro de Blueprints
    #
    # Blueprints sao "modulos de rotas" que agrupam endpoints
    # relacionados. Registramos aqui para que o Flask os conheca.
    #
    # url_prefix='/api' faz com que TODAS as rotas do Blueprint
    # comecem com /api (ex: /api/veiculos, /api/veiculos/1, etc.)
    # ----------------------------------------------------------
    app.register_blueprint(veiculos_bp, url_prefix='/api')
    app.register_blueprint(funcionarios_bp, url_prefix='/api')
    app.register_blueprint(estados_bp, url_prefix='/api')
    app.register_blueprint(servicos_prestados_bp, url_prefix='/api')
    app.register_blueprint(historico_ordem_servico_bp, url_prefix='/api')
    app.register_blueprint(clientes_bp, url_prefix='/api')
    app.register_blueprint(catalogo_servicos_bp, url_prefix='/api')
    app.register_blueprint(ordens_bp, url_prefix='/api')

    return app


if __name__ == '__main__':
    # Cria e inicia o servidor apenas quando executado diretamente:
    #   python run.py
    # Nunca quando importado por outro modulo (ex: durante testes).
    app = create_app()

    # debug=True e recarrega automaticamente ao salvar e mostra
    # erros detalhados. Use SOMENTE em desenvolvimento!
    app.run(debug=True)
