const fs = require('fs'); 
const equipamentos = [
{
"codigo": "MAT-001",
"descricao": "Cimento CP II-Z 50kg",
"quantidade": 150,
"valorUnitario": 34.90
},
{
"codigo": "MAT-002",
"descricao": "Tijolo Cerâmico 9x19x19cm",
"quantidade": 2500,
"valorUnitario": 1.25
},
{
"codigo": "MAT-003",
"descricao": "Areia Média Fina m³",
"quantidade": 12,
"valorUnitario": 110.00
},
{
"codigo": "MAT-004",
"descricao": "Tubo PVC 100mm 6m",
"quantidade": 40,
"valorUnitario": 48.50
},
{
"codigo": "MAT-005",
"descricao": "Cabo Flexível 2,5mm² 100m",
"quantidade": 8,
"valorUnitario": 189.90
}
]

// Salvar 
const dadosJson = JSON.stringify(equipamentos, null, 2);
fs.writeFileSync('equipamentos.json', dadosJson);
console.log('Equipamentos cadastrados com sucesso');

// Ler 
const dadosTexto = fs.readFileSync('equipamentos.json', 'utf-8');
const estoque = JSON.parse(dadosTexto); 

function Calcule(json) {
    if(json){
        console.log("--- Estoque ---")
            for (let i of json) {
                total = i.quantidade * i.valorUnitario
                console.log (`Código: ${i.codigo}`)
                console.log (`Descricao: ${i.descricao}`)
                console.log (`Quantidade: ${i.quantidade}`)
                console.log (`Valor Unitario: ${i.valorUnitario}`)
                console.log (`Total: ${total.toFixed(2)}\n`)
            } 
        }else {
            console.log(`Arquivo não encontrado`);
    }
};

Calcule(estoque);
