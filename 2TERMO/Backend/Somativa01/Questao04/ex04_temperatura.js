const entrada = require('readline-sync')

console.log("--- CLASSIFICACAO DE TEMPERATURA ---")
const temp = entrada.questionFloat("Digite a temperatura: ")

console.log(`\nTemperatura registrada: ${temp}°C`)
if (temp <= 60) {
    console.log("Status: NORMAL")
} else if (temp >= 61 && temp <= 80) {
    console.log("Status: ATENCAO")
} else {
    console.log("Status: CRITICA")
}