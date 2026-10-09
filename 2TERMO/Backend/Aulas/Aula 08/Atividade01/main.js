// Atividade 1: A Casa de Câmbio (Fixação de Sintaxe)
// Foco: Exportar e importar uma função simples com o caminho correto.

// 1. Crie uma pasta chamada atividade1.
// 2. Crie o arquivo conversor.js (Módulo). Dentro dele, crie uma função que
// recebe um valor em Dólar e retorna em Real (considere o dólar a R$ 5,00).
// 3. Exporte essa função.
// 4. Crie o arquivo app.js. Peça o valor em dólar ao usuário, use a ferramenta do
// módulo e mostre o resultado.

const entrada = require('readline-sync');
const calculo = require('./conversor');

console.log ("=== Conversor Dolar p/ Real ===")
const dolar = entrada.questionFloat("Digite o valor em dolar: ")
real = calculo.ConversorReal(dolar)

console.log (`\nValor em dolar: ${dolar.toFixed(2)}`)
console.log (`Valor em real: ${real.toFixed(2)}`)
