const fs = require('fs'); // Biblioteca de gravação e leitura de arquivo 

//  Mock - Dados já existentes/determinados (Usado para testes)
const produtos = [
    {id:1, nome: "Parafuso", qtd: 100},
    {id:2, nome: "Porca", qtd: 250},
    {id:3, nome: "Parafuso", qtd: 50}
];

function salvarDados() {
    // JSON.stringify - Grava as informações em um formato de banco de dados
    // null - Permite que a função seja filtrada 
    // 2 - Quebra linha pelas vírgula dentro do documento json 
    const dadosTexto = JSON.stringify(produtos, null, 2);  // stringify - Armazena 

    fs.writeFileSync('Estoque.json', dadosTexto); // fs.writeFileSync - Sincroniza com um arquivo json 
    console.log("Dados salvos com sucesso no arquivo estoque.json!");
}

function verEstoqueBaixo() {
    console.log("\n--- Produtos com estoque baixo (menos de 100) ---");

    // p - Pega inicial da variável - produtos
    // p.qtd - qtd dentro da variável produtos 
    const baixoEstoque = produtos.filter(p => p.qtd < 100); // Função de filtro na lista produtos
    console.log(baixoEstoque);
}

salvarDados(); // Executar as funções 
verEstoqueBaixo(); // Executar as funções 


