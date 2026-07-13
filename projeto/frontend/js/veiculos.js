// frontend/js/veiculos.js

document.addEventListener("DOMContentLoaded", () => {
    const tabelaBody = document.getElementById("tabela-veiculos-body");

    carregarVeiculos();

    async function carregarVeiculos() {
        try {
            const veiculos = await listarVeiculos();
            tabelaBody.innerHTML = ""; 

            if (veiculos.length === 0) {
                tabelaBody.innerHTML = `<tr><td colspan="5" style="text-align:center;">Nenhum veículo cadastrado.</td></tr>`;
                return;
            }

            veiculos.forEach(veiculo => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${veiculo.placa}</td>
                    <td>${veiculo.marca}</td>
                    <td>${veiculo.modelo}</td>
                    <td>${veiculo.ano || "-"}</td>
                    <td>${veiculo.nome_cliente || "Sem Proprietário Vinculado"}</td>
                `;
                tabelaBody.appendChild(tr);
            });
        } catch (erro) {
            console.error("Erro ao carregar veículos", erro);
            tabelaBody.innerHTML = `<tr><td colspan="5" style="text-align:center;color:red;">Erro ao carregar veículos.</td></tr>`;
        }
    }
});
