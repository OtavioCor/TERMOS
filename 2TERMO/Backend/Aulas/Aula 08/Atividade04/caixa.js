const entrada = require('readline-sync');
const calculo = require('./calculosVenda');

const name = entrada.question("Digite seu nome: ");
const valor = entrada.questionFloat("Digite o valor:");
const quantidade = entrada.questionInt("Digite o quantidade:");

const total = calculo.calcularTotal(valor, quantidade)
const cupom = calculo.gerarCupom(name, total)

console.log(`${cupom}`)
