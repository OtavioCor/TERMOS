// • O Verificador de Votação (Básico)
// • Objetivo: Praticar `if/else` simples.
// • Enunciado: Crie um programa que peça o nome do usuário e o
// ano de nascimento. O programa deve calcular a idade e dizer se
// ele já tem idade mínima para votar (16 anos).

const entrada = require('readline-sync');

console.log("--- VERIFICADOR DE VOTACAO ---")

const nome = entrada.question("Digite seu nome: ");
const idade = entrada.questionInt("Digite sua idade: ");

if (idade >= 16) {
    console.log(`\nOla ${nome}, voce tem a idade minima para votar!`);
} else {
    console.log(`\nOla ${nome}, voce NÃO tem a idade minima para votar!`);
}