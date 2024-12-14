async function mostrarDetalhes(produtoId) {
    try {
        const response = await fetch(`/produtos/detalhe/${produtoId}`);
        if (!response.ok) {
            alert("Erro ao carregar os detalhes do produto.");
            return;
        }
        const produto = await response.json();
        
        // Atualiza os elementos do HTML com os dados do produto
        document.getElementById("detalhes-nome").textContent = produto.nome;
        document.getElementById("detalhes-descricao").textContent = produto.descricao || "Sem descrição disponível.";
        document.getElementById("detalhes-preco").textContent = produto.preco;
        document.getElementById("detalhes-estoque").textContent = produto.estoque;

        // Mostra o contêiner de detalhes
        document.getElementById("detalhes-produto").style.display = "block";
    } catch (error) {
        console.error("Erro:", error);
        alert("Erro ao carregar os detalhes do produto.");
    }
}

function fecharDetalhes() {
    document.getElementById("detalhes-produto").style.display = "none";
}
