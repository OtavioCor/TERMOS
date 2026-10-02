const fs = require('fs'); 

const dadosTexto = fs.readFileSync('equipamentos.json', 'utf-8');
const equipamentos = JSON.parse(dadosTexto); 

function verificarArquivoJson(json){
    if(json){
        for (let i of json) {
            console.log (`Código: ${i.codigo}`)
            console.log (`Nome: ${i.nome}`)
            console.log (`Setor: ${i.setor}`)
            if (i.operacional === true){
                console.log (`Operacional: OPERACIONAL\n`)
            } else {
                console.log (`Operacional: PARADA\n`)
            }
        } 
        }else {
            console.log(`Arquivo não encontrado`);
    }
};

verificarArquivoJson(equipamentos)
