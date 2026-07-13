// frontend/js/cadastro_veiculo.js
// Script para validar e submeter o formulário de cadastro de veículos
// Requer que js/api.js esteja carregado antes no HTML

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-veiculo");
    const feedbackMsg = document.getElementById("feedback-message");
    const btnSalvar = document.getElementById("btn-salvar");

    if (form) {
        form.addEventListener("submit", async (event) => {
            // Previne o recarregamento padrão da página ao submeter o formulário
            event.preventDefault();

            // Reseta mensagens antigas e bloqueia o botão para evitar duplicação
            esconderFeedback();
            btnSalvar.disabled = true;
            btnSalvar.innerHTML = "Salvando...";

            // Captura os dados inseridos pelo usuário no formulário
            const placa = document.getElementById("placa").value.trim();
            const modelo = document.getElementById("modelo").value.trim();
            const marca = document.getElementById("marca").value.trim();
            const anoInput = document.getElementById("ano").value.trim();
            
            // O ano é opcional. Se preenchido, converte para número (base 10)
            const ano = anoInput ? parseInt(anoInput, 10) : null;

            // Monta o objeto JSON
            const dadosVeiculo = {
                placa,
                modelo,
                marca,
                ano
            };

            try {
                // Chama a função cadastrarVeiculo (já implementada em js/api.js)
                const resultado = await cadastrarVeiculo(dadosVeiculo);
                
                // Exibe a mensagem de sucesso retornada pela API
                mostrarFeedback(resultado.mensagem || "Veículo salvo com sucesso!", "success");
                
                // Limpa todos os campos do formulário após o sucesso
                form.reset();

            } catch (erro) {
                // Exibe o erro (pode ser retornado pela API ou erro de rede/CORS)
                mostrarFeedback(erro.message || "Erro ao salvar veículo. Tente novamente.", "error");
            } finally {
                // Restaura o estado e o texto do botão salvar
                btnSalvar.disabled = false;
                btnSalvar.innerHTML = `<span class="icon">✓</span> Salvar Veículo`;
            }
        });
    }

    /**
     * Exibe uma caixa de mensagem de feedback (Sucesso ou Erro) acima do form
     * @param {string} mensagem - O texto que será exibido
     * @param {string} tipo - Deve ser "success" ou "error"
     */
    function mostrarFeedback(mensagem, tipo) {
        feedbackMsg.textContent = mensagem;
        feedbackMsg.className = ""; // Limpa qualquer classe que estava (como a 'hidden')
        
        // Atribui a classe de cor baseada no tipo da resposta
        if (tipo === "success") {
            feedbackMsg.classList.add("success-message");
        } else {
            feedbackMsg.classList.add("error-message");
        }
    }

    /**
     * Esconde a caixa de mensagem de feedback
     */
    function esconderFeedback() {
        feedbackMsg.textContent = "";
        feedbackMsg.className = "hidden";
    }
});
