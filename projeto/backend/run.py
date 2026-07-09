# run.py - Entrypoint (Arquivo Principal) do Servidor Flask
#
# É aqui que a aplicação "nasce". Toda configuração global,
# registro de Blueprints (grupos de rotas) e inicialização
# do servidor acontecem neste arquivo.

from flask import Flask
from flask_cors import CORS
from app.routes.veiculos_routes import veiculos_bp  # Importa o Blueprint de veículos
from app.routes.funcionarios_routes import funcionarios_bp
from app.routes.estados_routes import estados_bp
from app.routes.servicos_prestados_routes import servicos_prestados_bp
from app.routes.historico_ordem_servico_routes import historico_ordem_servico_bp


def create_app():
    """
    Fábrica da aplicação Flask (padrão Application Factory).

    Em vez de criar o 'app' diretamente no escopo global,
    usamos uma função para criá-lo. Isso torna o código
    mais testável, flexível e escalável.

    Returns:
        Flask: instância configurada da aplicação.
    """
    app = Flask(__name__)
    
    # Ativa o CORS para permitir requisições do frontend (HTML/JS)
    CORS(app)

    # ----------------------------------------------------------
    # Registro de Blueprints
    #
    # Blueprints são "módulos de rotas" que agrupam endpoints
    # relacionados. Registramos aqui para que o Flask os conheça.
    #
    # url_prefix='/api' faz com que TODAS as rotas do Blueprint
    # comecem com /api (ex: /api/veiculos, /api/veiculos/1, etc.)
    # ----------------------------------------------------------
    app.register_blueprint(veiculos_bp, url_prefix='/api')
    app.register_blueprint(funcionarios_bp, url_prefix='/api')
    app.register_blueprint(estados_bp, url_prefix='/api')
    app.register_blueprint(servicos_prestados_bp, url_prefix='/api')
    app.register_blueprint(historico_ordem_servico_bp, url_prefix='/api')

    return app


if __name__ == '__main__':
    # Cria e inicia o servidor apenas quando executado diretamente:
    #   python run.py
    # Nunca quando importado por outro módulo (ex: durante testes).
    app = create_app()

    # debug=True → recarrega automaticamente ao salvar e mostra
    # erros detalhados. Use SOMENTE em desenvolvimento!
    app.run(debug=True)
