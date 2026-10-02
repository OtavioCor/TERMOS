// "Agora vamos criar um sistema para o setor de segurança. Precisamos de um
// módulo chamado sensor.js que tenha duas ferramentas:"
// 1. checarTemperatura(valor): Se for maior que 40, retorna "ALERTA: Caldeira
// Superaquecida".
// 2. checarUmidade(valor): Se for menor que 20, retorna "ALERTA: Ar muito seco".

// Instrução: No arquivo principal.js, peça os dois valores ao usuário e use as
// ferramentas do módulo para exibir os avisos.

const entrada = require('readline-sync');
const calculo = require('./sensor');

console.log("=== Verificaor de Temperatura e Umidade ===")
const calor = entrada.questionFloat("Digite a temperatura: ")
const molhado = entrada.questionFloat("Digite a umidade: ")

temp = calculo.checarTemperatura(calor)
umid = calculo.checarUmidade(molhado)

console.log(`\n${temp}`)
console.log(`${umid}`)