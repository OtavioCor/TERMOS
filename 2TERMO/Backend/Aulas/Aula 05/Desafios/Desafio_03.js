// Desafio 3

// Desafio 3: Calculadora de Área de Terrenos (Funções)
// Objetivo: Criar uma função que recebe parâmetros e
// retorna um valor.
// Enunciado: Crie uma função chamada calcularArea que
// receba a largura e o comprimento de um terreno e retorne
// a área total (largura * comprimento). No programa
// principal, peça os dados de 3 terrenos diferentes ao
// usuário, chame a função para cada um e mostre o
// resultado.

const entrada = require("readline-sync")

console.log("Calculadora de Área de Terrenos (Funções)")

for (let i = 1; i < 4; i++) {
    Area = 0

    const largura = entrada.questionFloat("Digite a largura: ");
    const comprimento = entrada.questionFloat("Digite o comprimento: ")

    function CalculoDeArea(a, b) {
        let Area = a * b;
        return Area; // Devolve o resultado para quem chamou
    }
    areatotal = CalculoDeArea(largura, comprimento)

    console.log(`---Terreno ${i}---\nLargura: ${largura}\nAltura: ${comprimento}\nArea total: ${areatotal}\n`)
}
