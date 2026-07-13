// frontend/js/admin_servicos.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-servico");
    const tabelaBody = document.getElementById("tabela-servicos-body");
    const feedbackMsg = document.getElementById("feedback-message");
    const btnSalvar = document.getElementById("btn-salvar");

    // Carregar a lista inicial de serviços
    carregarServicos();

    if (form) {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();

            esconderFeedback();
            btnSalvar.disabled = true;
            btnSalvar.innerHTML = "Salvando...";

            const nome = document.getElementById("nome").value.trim();
            const descricao = document.getElementById("descricao").value.trim();
            const preco = document.getElementById("preco").value.trim();

            const dadosServico = { nome, descricao, preco };

            try {
                const resultado = await criarServicoCatalogo(dadosServico);
                mostrarFeedback(resultado.mensagem || "Serviço criado com sucesso!", "success");
                form.reset();
                // Atualizar tabela
                carregarServicos();
            } catch (erro) {
                mostrarFeedback(erro.message || "Erro ao criar serviço.", "error");
            } finally {
                btnSalvar.disabled = false;
                btnSalvar.innerHTML = `Criar Serviço`;
            }
        });
    }

    async function carregarServicos() {
        try {
            const servicos = await listarServicosCatalogo();
            tabelaBody.innerHTML = ""; // Limpa a tabela

            if (servicos.length === 0) {
                tabelaBody.innerHTML = `<tr><td colspan="4" style="text-align:center;">Nenhum serviço cadastrado.</td></tr>`;
                return;
            }

            servicos.forEach(servico => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${servico.nome}</td>
                    <td>${servico.descricao || "-"}</td>
                    <td>R$ ${servico.preco.toFixed(2)}</td>
                    <td>
                        <button class="btn-danger" onclick="apagarServico('${servico.id}')">Apagar</button>
                    </td>
                `;
                tabelaBody.appendChild(tr);
            });
        } catch (erro) {
            console.error("Erro ao carregar serviços", erro);
        }
    }

    window.apagarServico = async function(id) {
        if (!confirm("Tem certeza que deseja apagar este serviço?")) return;

        try {
            await apagarServicoCatalogo(id);
            alert("Serviço apagado com sucesso.");
            carregarServicos();
        } catch (erro) {
            alert(erro.message || "Erro ao apagar serviço.");
        }
    };

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
