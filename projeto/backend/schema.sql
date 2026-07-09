-- 1. Clientes (Suporta múltiplos carros por cliente)
CREATE TABLE clientes (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT,
    cpf_cnpj TEXT UNIQUE,
    token_acesso TEXT, -- Usado para o login automático (Magic Link)
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Funcionários (Controle de permissões por setor)
CREATE TABLE funcionarios (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    setor TEXT NOT NULL CHECK(setor IN ('MECANICA', 'ESTETICA', 'RECEPCAO', 'GERENTE')),
    ativo BOOLEAN DEFAULT 1,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Veículos (Ligação 1:N com Clientes)
CREATE TABLE veiculos (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    placa TEXT UNIQUE NOT NULL,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER,
    cliente_id TEXT REFERENCES clientes(id) ON DELETE CASCADE
);

-- 4. Estados (Estados padrão do sistema + customizados da oficina)
CREATE TABLE estados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT DEFAULT 'PADRAO' CHECK(tipo IN ('PADRAO', 'CUSTOMIZADO')),
    setor_alvo TEXT DEFAULT 'AMBOS' CHECK(setor_alvo IN ('MECANICA', 'ESTETICA', 'AMBOS'))
);

-- 5. Ordens de Serviço (Controle central da Fila e Complicações)
CREATE TABLE ordens_servico (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    veiculo_id TEXT REFERENCES veiculos(id),
    estado_id INTEGER REFERENCES estados(id),
    fase_atual TEXT NOT NULL CHECK(fase_atual IN ('MECANICA', 'ESTETICA', 'PRONTO')),
    posicao_fila INTEGER,
    tem_complicacao BOOLEAN DEFAULT 0,
    motivo_complicacao TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Serviços Prestados (Vinculação de tarefas específicas e responsáveis)
CREATE TABLE servicos_prestados (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    ordem_servico_id TEXT REFERENCES ordens_servico(id) ON DELETE CASCADE,
    funcionario_id TEXT REFERENCES funcionarios(id), -- Quem está executando
    descricao_servico TEXT NOT NULL,
    setor TEXT NOT NULL CHECK(setor IN ('MECANICA', 'ESTETICA')),
    status_servico TEXT DEFAULT 'PENDENTE' CHECK(status_servico IN ('PENDENTE', 'EM_ANDAMENTO', 'CONCLUIDO'))
);

-- 7. Histórico e Auditoria de Estados
CREATE TABLE historico_ordem_servico (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    ordem_servico_id TEXT REFERENCES ordens_servico(id) ON DELETE CASCADE,
    estado_id INTEGER REFERENCES estados(id),
    funcionario_id TEXT REFERENCES funcionarios(id),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- OTIMIZAÇÃO DE BANCO (Índices para Busca Global na Agenda)
CREATE INDEX idx_veiculos_placa ON veiculos(placa);
CREATE INDEX idx_clientes_nome ON clientes(nome);