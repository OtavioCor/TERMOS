// • Desafio 4: Classificação de Atleta (Múltiplas Condições)
// • Objetivo: Praticar `else if`.
// • Enunciado: Uma escola de natação precisa classificar seus
// alunos por idade:
// • 5 a 10 anos Infantil
// • 11 a 17 anos: Juvenil
// • 18 a 60 anos: Adulto
// • Acima de 60 anos: Sênior

const entrada = require('readline-sync');

console.log("--- CLASSIFICACAO DE ATLETA ---");

const idade = entrada.questionInt("Digite sua idade: ");

if (idade >= 5 && idade <= 10){
    console.log("Sua classificacao: Infantil 👶");
} else if (idade >= 11 && idade <= 17){
    console.log("Sua classificacao: Juvenil 👦");
} else if (idade >= 18 && idade <= 60){
    console.log("Sua classificacao: Adulto 🧑");
} else if (idade <= 4){
    console.log("Idade insuficiente");
} else {
    console.log("Sua classificacao: Senior 🧓");
}
    


