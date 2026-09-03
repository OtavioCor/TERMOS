// const fs = require('fs'); 
// const entrada = require('readline-sync');

// console.log("=== SISTEMA DE CONSULTA DE ESTOQUE ===\n");

// try { // Impede que o sistema pare do nada 
//     const dadosTexto = fs.readFileSync('Estoque.json', 'utf-8');
//     const produtos = JSON.parse(dadosTexto); // parse - Abre e verifica

//     const termoBusca = entrada.question("Digite o nome do produto para buscar: ");
//     const resultado = produtos.find(p => p.nome.toLowerCase() === termoBusca.toLowerCase()); // Procura o nome digitado 

//     if (resultado) { // if (resultado) = Se existir dentro do banco de dados
//         console.log("\n PRODUTO ENCONTRADO");
//         console.log(`ID: ${resultado.id}`);
//         console.log(`Nome: ${resultado.nome}`);
//         console.log(`Quantidade em estoque: ${resultado.qtd}`);

//     } else {
//         console.log("\nSinto muito. Produto não cadastrado no sistema");
//     }
// } catch(erro) { // Impede que o sistema pare do nada 
//     console.log("Erro ao acessar o banco de dados: " + erro.message);
// }

// ===================================================================================================================================

const fs = require('fs'); 
const entrada = require('readline-sync');

console.log("=== SISTEMA DE CONSULTA DE ESTOQUE ===\n");


const dadosTexto = fs.readFileSync('Estoque.json', 'utf-8');
const produtos = JSON.parse(dadosTexto); 

const termoBusca = entrada.question("Digite a quantidade maxima: ");

function verMenor() {
    console.log(`\n--- PRODUTOS COM ESTOQUE ABAIXO DE ${termoBusca} ---`);

    const menor = produtos.filter(p => p.qtd < termoBusca);
    console.log(menor);
}
verMenor();
