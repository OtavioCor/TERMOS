const fs = require('fs'); 
const equipamentos = [
  {
    "codigo": "SEN-001",
    "tipo": "Temperatura",
    "valor": 24.5,
    "unidade": "°C",
    "status": "alerta"
  },
  {
    "codigo": "SEN-002",
    "tipo": "Umidade",
    "valor": 68.0,
    "unidade": "%",
    "status": "normal"
  },
  {
    "codigo": "SEN-003",
    "tipo": "Pressao",
    "valor": 1013.2,
    "unidade": "hPa",
    "status": "normal"
  },
  {
    "codigo": "SEN-004",
    "tipo": "Vibracao",
    "valor": 8.7,
    "unidade": "mm/s",
    "status": "alerta"
  },
  {
    "codigo": "SEN-005",
    "tipo": "Nivel de Cobalto",
    "valor": 0.02,
    "unidade": "ppm",
    "status": "critico"
  }
]

// Salvar 
const dadosJson = JSON.stringify(equipamentos, null, 2);
fs.writeFileSync('equipamentos.json', dadosJson);
console.log('Equipamentos cadastrados com sucesso');

// Ler 
const dadosTexto = fs.readFileSync('equipamentos.json', 'utf-8');
const sensores = JSON.parse(dadosTexto); 

function Registro(json) {
    if(json){
        console.log("--- REGISTRO DE SENSORES ---")
            for (let i of json) {
                console.log (`Código: ${i.codigo}`)
                console.log (`Tipo: ${i.tipo}`)
                console.log (`Valor: ${i.valor}`)
                console.log (`Unidade: ${i.unidade}`)
                console.log (`Status: ${i.status}\n`)
            } 
        }else {
            console.log(`Arquivo não encontrado`);
    }
};

function Verificador(json) {
    if(json){
        console.log("--- SENSORES EM ALERTA ---")
            for (let i of json) {
                if (i.status === 'alerta') {
                    console.log (`Código: ${i.codigo}`)
                    console.log (`Tipo: ${i.tipo}`)
                    console.log (`Valor: ${i.valor}`)
                    console.log (`Unidade: ${i.unidade}`)
                    console.log (`Status: ${i.status}\n`)
                } else {
                    continue
                }
            } 
        }else {
            console.log(`Arquivo não encontrado`);
    }
}

Registro(sensores);
Verificador(sensores);
