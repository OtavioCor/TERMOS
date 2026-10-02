
const fs = require('fs');

const equipamentos = [
  {
    codigo: 'EQP-001',
    nome: 'Torno CNC',
    setor: 'Usinagem',
    operacional: true
  },
  {
    codigo: 'EQP-002',
    nome: 'Prensa Hidráulica 50T',
    setor: 'Estamparia',
    operacional: true
  },
  {
    codigo: 'EQP-003',
    nome: 'Robô de Solda',
    setor: 'Montagem',
    operacional: false
  }
];

const dadosJson = JSON.stringify(equipamentos, null, 2);

fs.writeFileSync('equipamentos.json', dadosJson);

console.log('Equipamentos cadastrados com sucesso');