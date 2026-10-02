const fs = require('fs')

const dadosTexto = fs.readFileSync('equipamentos.json', 'utf-8');
const produtos = JSON.parse(dadosTexto); 

console.log(" --- EQUIPAMENTOS PARADOS ---")

function ApenasFalso(json) {
    if(json){
        for (let i of json) {
            let contagem = 0
                if (i.operacional === true){
                    continue
                } else {
                    console.log (`Código: ${i.codigo}`)
                    console.log (`Nome: ${i.nome}`)
                    console.log (`Setor: ${i.setor}`)
                    console.log (`Operacional: PARADA\n`)
                    contagem =+ 1
                }
            if (contagem > 0){
                console.log(`Equipamentos parados: ${contagem}`);
            } else {
                console.log("Nenhum equipamento parado");
            }
        } 
        }else {
            console.log(`Arquivo nao encontrado`);
    }
}

ApenasFalso(produtos);