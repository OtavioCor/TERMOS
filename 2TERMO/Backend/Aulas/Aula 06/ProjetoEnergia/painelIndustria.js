const entrada = require('readline-sync');
const calculo = require('./calculoEnergia');

console.log("=== MONITOR DE EFICIENCIA ENERGETICA ===");

const nome = entrada.question("Nome da maquina: ");
const potencia = entrada.questionInt("Potencia em Watts: ");
const horas = entrada.questionInt("Horas de uso no mes: ");
const preco = entrada.questionFloat("Preco do kWh: R$");

const consumoTotal = calculo.calcularKwh(potencia, horas);
const custo = calculo.calcularCusto(consumoTotal, preco);
const classificacao = calculo.classificarConsumo(consumoTotal);

console.log(" ----- RELATÓRIO -----")
console.log(`Máquina: ${nome.toUpperCase()}`);
console.log(`Consumo total: ${consumoTotal.toFixed(2)}`);
console.log(`Custo: R$ ${custo.toFixed(2)}`);
console.log(`Classificacao de consumo: ${classificacao}`);
console.log("-".repeat(35));