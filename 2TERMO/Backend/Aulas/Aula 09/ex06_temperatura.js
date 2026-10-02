const fs = require('fs'); 

const temperatura = [210, 250, 180, 390];

const dadosJson = JSON.stringify(temperatura, null, 2);
fs.writeFileSync('temperatura.json', dadosJson);
console.log('Medições cadastradas com sucesso!\n');

const dadosTexto = fs.readFileSync('temperatura.json', 'utf-8');
const registro = JSON.parse(dadosTexto);

function Controle(json) {
    if (json) {
        console.log("--- Controle de Temperatura ---");
        for (let i of json) {
            
            if (i <= 350) {
                console.log(`[NORMAL] Temperatura: ${i} °C`);
            } else {
                
                throw new Error(`ALERTA CRÍTICO: Temperatura de ${i} °C ultrapassou o limite operacional de 350 °C!`);
            }
        } 
    } else {
        console.log(`Arquivo não encontrado`);
    }
}

Controle();