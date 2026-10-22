const fs = require('fs');
const entrada = require('readline-sync');

console.log("--- SISTEMA DE REGISTRO DE FERRAMENTAS ---");
listaferramentas = [];
const qtd = entrada.questionInt("Quantidade de ferramentas: ");

for (let i = 0; i < qtd; i++){
    const nome = entrada.question("\nNome: ")
    const quantidade = entrada.questionInt("Quantidade:: ")
    const custoUnitario = entrada.questionFloat("Custo Unitario: ")

    listaferramentas.push(
        {
            nome: nome,
            quantidade: quantidade,
            custoUnitario: custoUnitario
        }
    );

    
}

fs.writeFileSync('ferramentas.json', JSON.stringify(listaferramentas, null, 2));

console.log(`Arquivo 'ferramentas.json' salvo com sucesso!`);

