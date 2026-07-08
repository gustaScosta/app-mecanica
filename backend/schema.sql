-- Estrutura do Banco de Dados SQLite (schema.sql)

-- Tabela de Usuários (Clientes)
CREATE TABLE IF NOT EXISTS usuario (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Telefone INTEGER NOT NULL,
    Endereco TEXT NOT NULL,
    CPF TEXT NOT NULL UNIQUE CHECK(length(CPF) <= 11 AND CPF NOT GLOB '*[^0-9]*')
);

-- Tabela de Carros (Veículos)
CREATE TABLE IF NOT EXISTS carro (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    placa TEXT NOT NULL UNIQUE,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER NOT NULL
    
    -- Caso precise relacionar o carro ao usuário (Dono do carro) futuramente, 
    -- você pode descomentar as linhas abaixo:
    -- , usuario_id INTEGER
    -- , FOREIGN KEY (usuario_id) REFERENCES usuario (Id)
);
