const entrada = require('readline-sync')

console.log("--- TABELA DE PRODUCAO ---")
const umciclo = entrada.question("Digite quantas pecas sao produzidas por ciclo: ")

for (i = 1; i <= 10; i++){
    let ciclo = console.log(`${i}° ciclo = ${i * umciclo}`)
}