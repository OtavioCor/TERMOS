// Desafio 2

// Desafio 2: O Gerador de Parcelas (Laços de Repetição)
// Objetivo: Praticar o uso do laço for e cálculos
// matemáticos.
// Enunciado: Uma loja de ferramentas quer mostrar ao
// cliente o valor das parcelas de uma compra. Peça o valor
// total do produto e a quantidade de parcelas (máximo 12).
// Use um loop para imprimir na tela o valor de cada parcela.
// - Exemplo: "Parcela 1: R 50,00", "Parcela 2: R 50,00"...


const entrada = require("readline-sync")

console.log("O Gerador de Parcelas (Laços de Repetição)")

const preco = entrada.questionInt("Digite o valor do produto: ");
const parcela = entrada.questionInt("Digite quantas parcelas deseja: ")
const precoparcela = preco / parcela

if (parcela <= 12){
    for (let i = 0; i <= parcela; i++) {
    console.log(`Parcela ${i}: R$ ${precoparcela.toFixed(2)}`);
    }
} else {
    console.log("INVALIDO! No maximo 12 parcelas")
}

