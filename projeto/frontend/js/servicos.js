// frontend/js/servicos.js

document.addEventListener("DOMContentLoaded", () => {
    const tabelaBody = document.getElementById("tabela-ordens-body");

    carregarOrdens();

    async function carregarOrdens() {
        try {
            const ordens = await listarOrdens();
            tabelaBody.innerHTML = ""; 

            if (ordens.length === 0) {
                tabelaBody.innerHTML = `<tr><td colspan="5" style="text-align:center;">Nenhuma ordem de serviço na fila.</td></tr>`;
                return;
            }

            ordens.forEach(ordem => {
                const tr = document.createElement("tr");
                const alerta = ordem.tem_complicacao ? `<span style="color:red;font-weight:bold;">⚠️ Sim</span>` : "Não";
                
                tr.innerHTML = `
                    <td>${ordem.id.substring(0, 8)}...</td>
                    <td>${ordem.modelo} (${ordem.placa})</td>
                    <td>${ordem.cliente_nome}</td>
                    <td><span style="background-color:var(--accent-glow);color:white;padding:3px 8px;border-radius:10px;font-size:0.8rem;">${ordem.fase_atual}</span></td>
                    <td>${alerta}</td>
                `;
                tabelaBody.appendChild(tr);
            });
        } catch (erro) {
            console.error("Erro ao carregar ordens", erro);
            tabelaBody.innerHTML = `<tr><td colspan="5" style="text-align:center;color:red;">Erro ao carregar ordens de serviço.</td></tr>`;
        }
    }
});
