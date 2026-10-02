const fs = require('fs'); 

const temperatura = [210, 250, 180, 390];

const dadosJson = JSON.stringify(temperatura, null, 2);
fs.writeFileSync('temperatura.json', dadosJson);
console.log('Medições cadastradas com sucesso!\n');

const fs = require('fs');



