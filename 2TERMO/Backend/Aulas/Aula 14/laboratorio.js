// 2. Leia o arquivo como texto
// No arquivo laboratorio.js, digite:

// const fs = require('fs');

// const texto = fs.readFileSync('maquinas.json', 'utf8'); 

// const maquinas = JSON.parse(texto); 

// console.log(typeof maquinas); 
// console.log(maquinas);       

// 3. Transforme o texto em dados JavaScript
// Substitua o código de laboratorio.js por:

// const fs = require("fs");
// const texto = fs.readFileSync("maquinas.json", "utf8");
// const maquinas = JSON.parse(texto);
// console.log(Array.isArray(maquinas));
// console.log(maquinas.length);
// console.log(maquinas[0].nome);

// 4. Listar registros com forEach()
// Mantenha a leitura e a conversão do exemplo anterior e substitua os três console.log() por:

// const fs = require("fs");
// const texto = fs.readFileSync("maquinas.json", "utf8");
// const maquinas = JSON.parse(texto);
// maquinas.forEach((maquina, indice) => {
// console.log(`${indice + 1}. ${maquina.nome}`);
// });

// 5. Buscar um único registro com find()
// Para evitar repetir o código de carregamento a cada exercício, mantenha as três instruções iniciais
// de leitura e conversão. Em seguida, digite:

// const fs = require("fs");
// const texto = fs.readFileSync("maquinas.json", "utf8");
// const maquinas = JSON.parse(texto);
// const procurada = maquinas.find(maquina => maquina.id === 2);
// console.log(procurada);

// 6. Selecionar vários registros com filter()
// Mantenha as instruções de carregamento e digite:

// const fs = require('fs');
// const texto = fs.readFileSync('maquinas.json', 'utf8');
// const maquinas = JSON.parse(texto);

// const emManutencao = maquinas.filter(maquina => maquina.status === 'Manutenção');

// console.log(emManutencao.length);
// console.log(emManutencao);

// 7. Compare os três métodos

// Não, o find() não serve para isso.
// • find() = Encontra apenas um (o primeiro).
// • filter() = Encontra todos.

// // 9. Treino opcional: tratando um erro de leitura
// const fs = require("fs");
// try {
// const texto = fs.readFileSync("maquinas.json", "utf8");
// const maquinas = JSON.parse(texto);
// console.log(`Registros carregados: ${maquinas.length}`);
// } catch (erro) {
// console.log("Não foi possível carregar os dados.");
// console.log(erro.message);
// }

console.log("--- DESAFIO A ---");
const fs = require("fs");
const texto = fs.readFileSync("maquinas.json", "utf8");
const maquinas = JSON.parse(texto);

maquinas.forEach(maquina => {
  console.log(`${maquina.id} | ${maquina.nome} | ${maquina.status}`);
});