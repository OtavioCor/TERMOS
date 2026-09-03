// Desafio 4

// Desafio 4: Catálogo de Filmes (Objetos e Arrays)
// Objetivo: Manipular listas de objetos e acessar suas propriedades.
// Enunciado: Crie um Array de Objetos chamado cinema. Cada
// objeto deve representar
// um filme e ter as propriedades: titulo e classificacao (idade
// mínima).
// Cadastre 3 filmes manualmente no código. Depois, peça a idade
// do usuário no terminal e use um loop para mostrar apenas os
// títulos dos filmes que ele tem idade para assistir.

const entrada = require("readline-sync");

console.log("Catálogo de Filmes");

const filme = ["Dora Aventureira - Live Action", "Jogos Vorazes: A Esperença", "Todo Mundo em Pânico"];
const classificacao = [12, 16, 18];

const idade = entrada.questionInt("Digite sua idade: ");

console.log("=== FILMES DISPONIVEIS ===");

for (let i = 0; i < filme.length; i++) {
    
    if (classificacao[i] <= idade) {
        console.log(`${filme[i]}`);
        
    } else {
        console.log("indisponivel");
    }

}

// --------------------------------- DO PROFESSOR -------------------------------------- //

const cinema = [ 
    { titulo: "Dumbo", censura: 0},
    { titulo: "Deadpool", censura: 18},
    { titulo: "Batman", censura: 12},
];
const idadeUser = entrada.questionInt("Qual sua idade? ");
for (let i = 0; i < cinema.length; i++) {
    if (idadeUser >= cinema[i].censura){
        console.log(`Pode ver: ${cinema[i].titulo}`);
    }
}
