// frontend/js/api.js
// Responsável por toda comunicação HTTP com a API do backend.
// Centralizar as chamadas aqui evita repetição de código e facilita
// trocar a URL base ou adicionar autenticação em um único lugar.

// URL base da API. Altere aqui caso o backend mude de endereço.
const API_BASE_URL = 'http://localhost:5000/api';

/**
 * Cadastra um novo veículo na API.
 *
 * @param {Object} dadosVeiculo - Objeto com os dados do veículo.
 * @param {string} dadosVeiculo.placa   - Placa do veículo (ex: "ABC-1234").
 * @param {string} dadosVeiculo.modelo  - Modelo do veículo (ex: "Gol").
 * @param {string} dadosVeiculo.marca   - Marca do veículo (ex: "Volkswagen").
 * @param {number} dadosVeiculo.ano     - Ano de fabricação (ex: 2020).
 *
 * @returns {Promise<Object>} Resposta da API em formato JSON.
 * @throws {Error} Lança um erro se a resposta da API não for bem-sucedida.
 *
 * Exemplo de uso:
 *   const resultado = await cadastrarVeiculo({ placa: 'ABC-1234', modelo: 'Gol', marca: 'VW', ano: 2020 });
 *   console.log(resultado.mensagem);
 */
async function cadastrarVeiculo(dadosVeiculo) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/veiculos`, {
      method: 'POST',

      // Informa ao backend que o corpo da requisição é JSON
      headers: {
        'Content-Type': 'application/json'
      },

      // Converte o objeto JS para string JSON antes de enviar
      body: JSON.stringify(dadosVeiculo)
    });

    // Converte a resposta da API para objeto JS
    const dados = await resposta.json();

    // Se o HTTP status não for 2xx (ex: 400, 500), lança um erro
    // com a mensagem retornada pelo backend
    if (!resposta.ok) {
      throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao cadastrar veículo.`);
    }

    return dados;

  } catch (erro) {
    // Relança o erro para ser tratado por quem chamou a função
    // (ex: mostrar uma mensagem de erro na tela para o usuário)
    console.error('[API] Erro em cadastrarVeiculo:', erro.message);
    throw erro;
  }
}

/**
 * Cadastra um novo funcionário na API.
 */
async function cadastrarFuncionario(dadosFuncionario) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/funcionarios`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosFuncionario)
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao cadastrar funcionário.`);
    return dados;
  } catch (erro) {
    console.error('[API] Erro em cadastrarFuncionario:', erro.message);
    throw erro;
  }
}

/**
 * Cadastra um novo estado na API.
 */
async function cadastrarEstado(dadosEstado) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/estados`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosEstado)
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao cadastrar estado.`);
    return dados;
  } catch (erro) {
    console.error('[API] Erro em cadastrarEstado:', erro.message);
    throw erro;
  }
}

/**
 * Cadastra um novo serviço prestado na API.
 */
async function cadastrarServicoPrestado(dadosServicoPrestado) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/servicos-prestados`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosServicoPrestado)
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao cadastrar serviço prestado.`);
    return dados;
  } catch (erro) {
    console.error('[API] Erro em cadastrarServicoPrestado:', erro.message);
    throw erro;
  }
}

/**
 * Cadastra um novo histórico de ordem de serviço na API.
 */
async function cadastrarHistoricoOrdemServico(dadosHistorico) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/historico-ordem-servico`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosHistorico)
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao cadastrar histórico de OS.`);
    return dados;
  } catch (erro) {
    console.error('[API] Erro em cadastrarHistoricoOrdemServico:', erro.message);
    throw erro;
  }
}

/**
 * Cadastra um novo cliente na API.
 */
async function cadastrarCliente(dadosCliente) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/clientes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosCliente)
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao cadastrar cliente.`);
    return dados;
  } catch (erro) {
    console.error('[API] Erro em cadastrarCliente:', erro.message);
    throw erro;
  }
}

/**
 * Lista todos os servicos no catalogo.
 */
async function listarServicosCatalogo() {
  try {
    const resposta = await fetch(`${API_BASE_URL}/catalogo-servicos`);
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao listar servicos.`);
    return dados.dados || [];
  } catch (erro) {
    console.error('[API] Erro em listarServicosCatalogo:', erro.message);
    throw erro;
  }
}

/**
 * Cria um novo servico no catalogo.
 */
async function criarServicoCatalogo(dadosServico) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/catalogo-servicos`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosServico)
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao criar servico.`);
    return dados;
  } catch (erro) {
    console.error('[API] Erro em criarServicoCatalogo:', erro.message);
    throw erro;
  }
}

/**
 * Apaga um servico do catalogo pelo id.
 */
async function apagarServicoCatalogo(id) {
  try {
    const resposta = await fetch(`${API_BASE_URL}/catalogo-servicos/${id}`, {
      method: 'DELETE'
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao apagar servico.`);
    return dados;
  } catch (erro) {
    console.error('[API] Erro em apagarServicoCatalogo:', erro.message);
    throw erro;
  }
}

/**
 * Lista todos os clientes.
 */
async function listarClientes() {
  try {
    const resposta = await fetch(`${API_BASE_URL}/clientes`);
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao listar clientes.`);
    return dados.dados || [];
  } catch (erro) {
    console.error('[API] Erro em listarClientes:', erro.message);
    throw erro;
  }
}

/**
 * Lista todos os veiculos.
 */
async function listarVeiculos() {
  try {
    const resposta = await fetch(`${API_BASE_URL}/veiculos`);
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao listar veiculos.`);
    return dados.dados || [];
  } catch (erro) {
    console.error('[API] Erro em listarVeiculos:', erro.message);
    throw erro;
  }
}

/**
 * Lista todas as ordens de servico da fila.
 */
async function listarOrdens() {
  try {
    const resposta = await fetch(`${API_BASE_URL}/ordens`);
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || `Erro ${resposta.status}: Falha ao listar ordens.`);
    return dados.dados || [];
  } catch (erro) {
    console.error('[API] Erro em listarOrdens:', erro.message);
    throw erro;
  }
}
