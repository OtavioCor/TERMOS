const entrada = require('readline-sync')

console.log("--- CALCULO DE MEDIA ---")

let total = 0

for (i = 1; i <= 5; i++){
    const valor = entrada.questionInt(`Digite o ${i} valor: `)
    total += valor
}

const media = total / 5

console.log(`Soma total: ${total}`)
console.log(`Media: ${media}`)