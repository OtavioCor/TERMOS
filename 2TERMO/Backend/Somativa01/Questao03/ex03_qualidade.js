const entrada = require('readline-sync')

console.log("--- PADRONIZACAO DE PECA ---")
const peso = entrada.questionFloat("Digite o peso: ")

console.log("\n--- REGISTRO ---")
if (peso >= 95 && peso <= 105) {
    console.log('PEÇA APROVADA ✅')
} else {
    console.log('PEÇA REPROVADA ❌')
}
console.log(`Peso registrado: ${peso}g`)
