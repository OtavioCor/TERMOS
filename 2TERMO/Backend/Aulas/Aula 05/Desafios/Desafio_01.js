// Desafio 1: O Verificador de Aposentadoria (Lógica e Decisão)
// Objetivo: Praticar cálculos, if/else e operadores lógicos.
// Enunciado: Crie um programa que peça o nome, a idade e o tempo de contribuição de um trabalhador.
// A regra para se aposentar é:
// Ter pelo menos 65 anos de idade.
// Ou ter pelo menos 30 anos de contribuição. 
// Exiba uma mensagem dizendo se o trabalhador já pode se aposentar ou não

const entrada = require("readline-sync")

console.log("O Verificador de Aposentadoria (Lógica e Decisão)")

const nome = entrada.question("Digite seu nome: ");
const idade = entrada.questionInt("Digite sua idade: ");
const contribuicao = entrada.questionInt("Digite seu tempo de contribuicao: ");

if (idade >= 65 || contribuicao >= 30) {
    console.log("Permitido aposentadoria")
} else {
    console.log("Negado aposentadoria")
}

