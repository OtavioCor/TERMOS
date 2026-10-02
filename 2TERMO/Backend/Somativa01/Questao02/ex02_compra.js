const entrada = require('readline-sync')

const material = entrada.question("Digite o nome do material: ")
const qtd = entrada.questionInt("Digite a quantidade comprada: ")
const unit = entrada.questionFloat("Digite o preco unitario: ")
const total = qtd * unit

console.log("--- CALCULO DE CUSTO ---")
console.log(`Material: ${material}\nQuantidade: ${qtd}\nPreco unitario: ${unit}\nCusto total: ${total}`)
