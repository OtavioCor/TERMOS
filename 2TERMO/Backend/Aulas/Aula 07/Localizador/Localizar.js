const fs = require('fs'); 
const entrada = require('readline-sync');

console.log("=== LOCALIZADOR DE CRACHÁS ===\n");

try{
    const dadosTexto = fs.readFileSync('funcionarios.json', 'utf-8');
    const funcionarios = JSON.parse(dadosTexto); // parse - Abre e verifica

    const cracha = entrada.question("Digite o ID: ");
    const pessoa = registro.find(r => r.id === cracha);

    console.log("LOCALIZADOR DE CRACHÁS");

    
    
if (pessoa) { 
    console.log("\n FUNCIONARIO ENCONTRADO");
    console.log(`ID: ${pessoa.id}`);
    console.log(`Nome: ${pessoa.nome}`);
    console.log(`Quantidade em estoque: ${pessoa.qtd}`);
} else {
    console.log("Acesso Negado: ID não encontrado");
}
} catch(erro) { 
    console.log("Erro ao acessar o banco de dados: " + erro.message);
}


