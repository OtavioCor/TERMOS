// • O "Mão de Vaca" (Cálculo com Decisão)
// • Objetivo:** Praticar cálculos e `if/else`.
// • Enunciado: Um restaurante está dando 10% de desconto para
// contas acima de R$ 100,00. Peça o valor total da conta. Se for
// acima de 100, mostre o valor com desconto. Se for abaixo, mostre
// o valor normal.

const entrada = require('readline-sync');

console.log("--- CALCULO DE PROMOCAO ---");

const conta = entrada.questionInt("Digite o valor total para avaliar o desconto: ");

if (conta > 100) { 
    console.log(`Voce ganhou 10% de desconto 😊! Valor total: ${conta * 0.9}`);
} else {
    console.log(`Sem desconto😭 Valor total: ${conta}`);
}


