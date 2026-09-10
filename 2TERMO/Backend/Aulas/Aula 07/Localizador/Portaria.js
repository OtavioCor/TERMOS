const fs = require('fs');

const registro = [
    {id:101, nome: "Leonardo", setor: "DEVIS"},
    {id:102, nome: "Sugiro", setor: "Usinagem"},
    {id:103, nome: "Bruno", setor: "Mecanica"},
    {id:104, nome: "Rebecca", setor: "DEVIS"}
];

function salvarDados() {
    const dadosTexto = JSON.stringify(registro, null, 2);  

    fs.writeFileSync('funcionarios.json', dadosTexto);  
    console.log("Dados salvos com sucesso no arquivo estoque.json!");
}


salvarDados();


