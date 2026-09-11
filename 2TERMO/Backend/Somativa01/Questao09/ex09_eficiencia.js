const entrada = require('readline-sync')

function calcularEficiencia(real, prevista) {
    return (real / prevista) * 100
}
function classificarEficiencia(percentual){
    if (percentual >= 90){
        return "META ATINGIDA"
    } else if (percentual >= 70 && percentual <= 89.99) {
        return "ATENCAO"
    } else {
        return "ABAIXO DA META"
    }
}

const prev = entrada.questionFloat("Digite a producao prevista: ")
const real = entrada.questionFloat("Digite a producao real: ")

const perc = calcularEficiencia(real, prev)
const clas = classificarEficiencia(perc)

console.log("---- CALCULO DE EFICIENCIA----")

console.log(`Producao real: ${real}`)
console.log(`Producao prevista: ${prev}`)
console.log(`Percentual: ${perc}%`)
console.log(`Classificacao: ${clas}`)

