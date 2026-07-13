// frontend/js/cadastro_cliente.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-cliente");
    const feedbackMsg = document.getElementById("feedback-message");
    const btnSalvar = document.getElementById("btn-salvar");

    if (form) {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();

            esconderFeedback();
            btnSalvar.disabled = true;
            btnSalvar.innerHTML = "Salvando...";

            const nome = document.getElementById("nome").value.trim();
            const idade = parseInt(document.getElementById("idade").value.trim(), 10);
            const cpf = document.getElementById("cpf").value.trim();
            const email = document.getElementById("email").value.trim();
            const senha = document.getElementById("senha").value.trim();

            const dadosCliente = { nome, idade, cpf, email, senha };

            try {
                // api.js deve estar carregado
                const resultado = await cadastrarCliente(dadosCliente);
                mostrarFeedback(resultado.mensagem || "Cliente salvo com sucesso!", "success");
                form.reset();
            } catch (erro) {
                mostrarFeedback(erro.message || "Erro ao salvar cliente. Tente novamente.", "error");
            } finally {
                btnSalvar.disabled = false;
                btnSalvar.innerHTML = `<span class="icon">✓</span> Salvar Cliente`;
            }
        });
    }

    function mostrarFeedback(mensagem, tipo) {
        feedbackMsg.textContent = mensagem;
        feedbackMsg.className = "";
        
        if (tipo === "success") {
            feedbackMsg.classList.add("success-message");
        } else {
            feedbackMsg.classList.add("error-message");
        }
    }

    function esconderFeedback() {
        feedbackMsg.textContent = "";
        feedbackMsg.className = "hidden";
    }
});
