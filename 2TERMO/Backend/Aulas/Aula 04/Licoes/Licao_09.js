// Desafio — Controle de Acesso ao Laboratório
// Uma escola possui um laboratório que só pode ser utilizado por alunos que atendam às regras de
// acesso.
// Crie um programa em JavaScript que pergunte:
// a idade do aluno;
// se ele possui autorização ( S ou N );
// se ele está acompanhado por um professor ( S ou N ).
// --- REGRAS ---
// O aluno poderá entrar no laboratório se:
// tiver 16 anos ou mais E possuir autorização OU stiver acompanhado por um professor.

const entrada = require('readline-sync');

console.log("Controle de Acesso ao Laboratório");

const idade = entrada.questionInt("Digite sua idade: \n");
const autorizacao = entrada.keyInYNStrict("Possui autorizacao: \n");
const professor = entrada.keyInYNStrict("Acompanhado com professor: \n");
const suspenso = entrada.keyInYNStrict("Esta suspenso:  \n");

if((idade >= 16 && autorizacao === true || professor === true) && suspenso === false) {
    console.log("Acesso autorizado");
} else{
    console.log("Acesso NEGADO");
}

// toUpperCase = deixa maiusculo automaticamente

// -----------------------------------------------------------------------------------------

// A do professor

// const entrada = require('readline-sync');

// console.log("Controle de Acesso ao Laboratório");

// const idade = entrada.questionInt("Digite sua idade: \n");
// const autorizacao = entrada.question("Possui autorizacao: \n").toUpperCase();
// const professor = entrada.question("Acompanhado com professor: \n").toUpperCase();

// if(idade >= 16 && autorizacao === "S" || professor === "S") {
//     console.log("Acesso LIBERADO");
// } else {
//     console.log("Acesso NEGADO");
// }

