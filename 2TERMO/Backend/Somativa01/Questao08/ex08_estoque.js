const entrada = require('readline-sync')

estoque = []
minimo = 50
console.log("--- REGISTRO DE ESTOQUE ---")
for (i = 1; i <= 3; i++){
    let nome = entrada.question("\nDigite o nome: ")
    let quantidade = entrada.questionInt("Digite a quantidade: ")
   
    estoque.push({
        nome: nome,
        quantidade: quantidade
    })
}

console.log("\n====== RELATORIO ======");
for (let i = 0; i < estoque.length; i++) {
    console.log(`\n${i + 1}° Componente - ${estoque[i].nome}\nQuantidade - (${estoque[i].quantidade})`);
    if (estoque[i].quantidade < minimo) {
        console.log('Status - REPOR ESTOQUE')
    } else {
        console.log('Status - ESTOQUE OK')
    }
}

