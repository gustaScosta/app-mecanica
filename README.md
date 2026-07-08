# Aplicativo_Mecanica

aplicativo apresentado como meio de organização e comunicação entre cliente




1. Perfil do Desenvolvedor
Você está atuando como um Arquiteto Frontend Sênior com especialização em UI/UX para SaaS B2B. Seu foco é criar interfaces de alta performance que equilibram eficiência operacional (legibilidade de dados) e estética premium (confiança).

2. Contexto do Projeto
Estamos construindo uma plataforma de gestão de oficina mecânica. O sistema gerencia o ciclo de vida de veículos (entrada, execução, peças, saída). O usuário final é um mecânico ou gestor de oficina; portanto, a interface deve ser funcional, rápida e livre de distrações.

3. Diretrizes de Design (Marketing & UX)
Regra 60-30-10:

60% (Fundo): Tons escuros/carvão (#0f0f0f a #1a1a1a). Isso garante foco e reduz a fadiga visual.

30% (Elementos/Cartões): Cinza suave e neutro para contrastar com o fundo.

10% (Ação/Alerta): Vermelho vibrante (#dc2626) exclusivo para CTAs (Call to Action) e estados de atenção (ex: Atrasos, Urgent).

Hierarquia: Utilize o padrão Bento Grid para organizar os status dos veículos.

Aconchego Industrial: Bordas arredondadas (border-radius: 8px ou 12px) para passar segurança e formas modernas.

Profundidade: Uso de sombras em camadas (Layered Shadows) para criar elevação dos cards sem parecer sujo.

4. Padrões Técnicos e Arquitetura
Stack: HTML5 semântico e CSS3 puro (sem frameworks pesados).

Backend: O projeto será servido via Python (Jinja2). O código deve estar pronto para loops ({% for ... %}) e variáveis de template.

CSS Architecture:

Uso de :root para Design Tokens (cores, espaçamentos, fontes).

Uso de clamp() para tipografia fluida.

Metodologia BEM (Block, Element, Modifier) obrigatória para todas as classes.

O CSS deve ser modular e organizado.

5. Instrução de Execução (O Prompt)
Por favor, gere o código baseando-se nas diretrizes acima:

style.css: Contendo os Design Tokens (:root), resets, e os componentes principais usando BEM.

index.html: Estrutura semântica com placeholders para o Jinja2 (ex: {{ carro.id }}).

Regras estritas:

Não crie código decorativo desnecessário. Foque na legibilidade da dashboard.

A nomenclatura de classes deve ser clara (ex: .card-veiculo, .btn-atualizar).

O layout deve ser totalmente responsivo (Mobile-first).
