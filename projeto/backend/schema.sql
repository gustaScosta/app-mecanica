-- 1. Clientes (Suporta multiplos carros por cliente)
CREATE TABLE IF NOT EXISTS clientes (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    nome TEXT NOT NULL,
    idade INTEGER,
    telefone TEXT,
    email TEXT,
    cpf TEXT UNIQUE,
    senha_hash TEXT,
    token_acesso TEXT, -- Usado para o login automatico (Magic Link)
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Funcionarios (Controle de permissoes por setor)
CREATE TABLE IF NOT EXISTS funcionarios (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    setor TEXT NOT NULL CHECK(setor IN ('MECANICA', 'ESTETICA', 'RECEPCAO', 'GERENTE')),
    ativo BOOLEAN DEFAULT 1,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Veiculos (Ligacao 1:N com Clientes)
CREATE TABLE IF NOT EXISTS veiculos (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    placa TEXT UNIQUE NOT NULL,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER,
    cliente_id TEXT REFERENCES clientes(id) ON DELETE CASCADE
);

-- 4. Estados (Estados padrao do sistema + customizados da oficina)
CREATE TABLE IF NOT EXISTS estados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT DEFAULT 'PADRAO' CHECK(tipo IN ('PADRAO', 'CUSTOMIZADO')),
    setor_alvo TEXT DEFAULT 'AMBOS' CHECK(setor_alvo IN ('MECANICA', 'ESTETICA', 'AMBOS'))
);

-- 5. Ordens de Servico (Controle central da Fila e Complicacoes)
CREATE TABLE IF NOT EXISTS ordens_servico (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    veiculo_id TEXT REFERENCES veiculos(id),
    estado_id INTEGER REFERENCES estados(id),
    fase_atual TEXT NOT NULL CHECK(fase_atual IN ('MECANICA', 'ESTETICA', 'PRONTO')),
    posicao_fila INTEGER,
    tem_complicacao BOOLEAN DEFAULT 0,
    motivo_complicacao TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Servicos Prestados (Vinculacao de tarefas especificas e responsaveis)
CREATE TABLE IF NOT EXISTS servicos_prestados (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    ordem_servico_id TEXT REFERENCES ordens_servico(id) ON DELETE CASCADE,
    funcionario_id TEXT REFERENCES funcionarios(id), -- Quem esta executando
    descricao_servico TEXT NOT NULL,
    setor TEXT NOT NULL CHECK(setor IN ('MECANICA', 'ESTETICA')),
    status_servico TEXT DEFAULT 'PENDENTE' CHECK(status_servico IN ('PENDENTE', 'EM_ANDAMENTO', 'CONCLUIDO'))
);

-- 7. Historico e Auditoria de Estados
CREATE TABLE IF NOT EXISTS historico_ordem_servico (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    ordem_servico_id TEXT REFERENCES ordens_servico(id) ON DELETE CASCADE,
    estado_id INTEGER REFERENCES estados(id),
    funcionario_id TEXT REFERENCES funcionarios(id),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- OTIMIZACAO DE BANCO (Indices para Busca Global na Agenda)
CREATE INDEX IF NOT EXISTS idx_veiculos_placa ON veiculos(placa);
CREATE INDEX IF NOT EXISTS idx_clientes_nome ON clientes(nome);

-- 8. Catalogo de Servicos (Servicos disponiveis para cadastro)
CREATE TABLE IF NOT EXISTS catalogo_servicos (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
