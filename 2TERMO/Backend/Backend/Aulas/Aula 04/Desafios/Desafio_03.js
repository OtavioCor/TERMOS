// • Álcool ou Gasolina? (Matemática + Lógica)
// • Objetivo: Praticar lógica aplicada ao dia a dia.
// • Enunciado: Dizem que só compensa abastecer com Álcool se o
// preço dele for menor que 70% do preço da Gasolina. Peça o preço
// do litro de cada um. O programa deve calcular: `precoAlcool /
// precoGasolina`. Se o resultado for menor que 0.7, mostre
// "Abasteça com ÁLCOOL". Caso contrário, mostre "Abasteça com
// GASOLINA".

const entrada = require('readline-sync');

console.log("--- ESCOLHA DE ABASTECIMENTO ---");

const precoalc = entrada.questionFloat("Digite o preco de 1li/Gasolina: ");
const precogas = entrada.questionFloat("Digite o preco de 1li/Alcool: ");

const preco = (precoalc / precogas);

if (preco < 0.7) {
    console.log("Abasteca com ALCOOL");
} else {
    console.log("Abasteca com GASOLINA");
}