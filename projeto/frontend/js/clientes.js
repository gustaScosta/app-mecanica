// frontend/js/clientes.js

document.addEventListener("DOMContentLoaded", () => {
    const tabelaBody = document.getElementById("tabela-clientes-body");

    carregarClientes();

    async function carregarClientes() {
        try {
            const clientes = await listarClientes();
            tabelaBody.innerHTML = ""; 

            if (clientes.length === 0) {
                tabelaBody.innerHTML = `<tr><td colspan="5" style="text-align:center;">Nenhum cliente cadastrado.</td></tr>`;
                return;
            }

            clientes.forEach(cliente => {
                const tr = document.createElement("tr");
                const dataFormatada = new Date(cliente.criado_em).toLocaleDateString('pt-BR', {
                    day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit'
                });
                
                tr.innerHTML = `
                    <td>${cliente.nome}</td>
                    <td>${cliente.idade || "-"}</td>
                    <td>${cliente.cpf}</td>
                    <td>${cliente.email}</td>
                    <td>${dataFormatada}</td>
                `;
                tabelaBody.appendChild(tr);
            });
        } catch (erro) {
            console.error("Erro ao carregar clientes", erro);
            tabelaBody.innerHTML = `<tr><td colspan="5" style="text-align:center;color:red;">Erro ao carregar clientes.</td></tr>`;
        }
    }
});
