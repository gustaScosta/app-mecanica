// frontend/js/app.js
// Script principal responsável pela interatividade e lógica da interface do usuário (UI)

document.addEventListener("DOMContentLoaded", () => {
    console.log("Interface principal MecaEste iniciada com sucesso!");

    /**
     * 1. Saudação Dinâmica
     * Altera o título de boas-vindas com base no horário do computador do usuário.
     */
    const welcomeMessage = document.getElementById('welcome-message');
    if (welcomeMessage) {
        const horaAtual = new Date().getHours();
        let saudacao = "Bem-vindo(a)";
        
        if (horaAtual >= 5 && horaAtual < 12) {
            saudacao = "Bom dia";
        } else if (horaAtual >= 12 && horaAtual < 18) {
            saudacao = "Boa tarde";
        } else {
            saudacao = "Boa noite";
        }
        
        // Mantém a personalização visual, injetando o texto no HTML
        welcomeMessage.textContent = `${saudacao} ao Sistema!`;
    }

    /**
     * 2. Log de Interação no Botão de Cadastro
     * Apenas para monitorar as intenções de clique (o redirecionamento nativo do HTML via tag <a> faz o resto).
     */
    const btnNovoVeiculo = document.getElementById('btn-novo-veiculo');
    if (btnNovoVeiculo) {
        btnNovoVeiculo.addEventListener('click', () => {
            console.log("Usuário navegando para a tela de Cadastro de Novo Veículo...");
        });
    }
});
