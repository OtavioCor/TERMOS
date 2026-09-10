const entrada = require('readline-sync');
const idade = entrada.questionInt("Qual sua idade? ");

if (idade >= 18) {
    console.log("Acesso liberado! Divirta-se.");
} else {
    console.log("Acesso negado. Vá para casa estudar Node.js!");
}