const entrada = require('readline-sync');

console.log("---Calculadora de IMC---");

const peso = entrada.questionFloat("Digite seu peso: ");
const altura = entrada.questionFloat("Digite sua altura: ");
 
const total = peso / altura ^ 2;

console.log(`Seu IMC: ${total.toFixed(1)}`);
