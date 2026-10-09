const entrada = require('readline-sync');

console.log("=== Balanca de Precisao Industrial ===");
const calculo = require('./funcoesBalanca');
while(true) {
    try {
        const peso = entrada.question("Digite o peso (ou 'sair'): ")
        
        if (peso.toLowerCase() === 'sair') {
        sistemaAtivo = false;
        console.log("Encerrando sistema...");
        break
        }
        
        const balanca = calculo.verificarPeso(peso);
        console.log(`Resultado: ${balanca}`)
        
    } catch (erro) {
        console.log(`⚠️ ALERTA: ${erro.message}`)
    }
} 