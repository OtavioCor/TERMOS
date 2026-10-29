// // EXERCÍCIO 1 - Preparar o laboratório
const { asyncWrapProviders } = require("async_hooks");
const fs = require("fs");
const { urlToHttpOptions } = require("url");

// // EXERCÍCIO 2 - Ler o arquivo como texto
const texto = fs.readFileSync("maquinas.json", "utf8");
console.log(typeof texto);
console.log(texto);

// // EXERCÍCIO 3 - Converter o texto em dados JavaScript
const maquinas = JSON.parse(texto);
console.log(Array.isArray(maquinas));
console.log(maquinas.length);
console.log(maquinas[0].nome);

// EXERCÍCIO 4 - Listar registros com forEach()
maquinas.forEach((maquina, indice) => {
  console.log(`${indice + 1}. ${maquina.nome} - ${maquina.setor} - ${maquina.status}`);
});

// // EXERCÍCIO 5 - Buscar um registro com find()
const procurada = maquinas.find(maquina => maquina.id === 2);
console.log(procurada);


// // EXERCÍCIO 6 - Selecionar registros com filter()
const emManutencao = maquinas.filter(
  maquina => maquina.status === "Manutenção"
);
console.log(emManutencao.length);
console.log(emManutencao);

// const paradas = maquinas.filter(
//   maquina => maquina.status === "Parada"
// );
// console.log(paradas);
// console.log(paradas.length);

// const usinagem = maquinas.filter(
//   maquina => maquina.setor === "Usinagem"
// );
// console.log(usinagem);

// const montagem = maquinas.filter(
//   maquina => maquina.setor === "Montagem"
// );
// console.log(montagem);

// // EXERCÍCIO 7 - Comparar os métodos
// console.log(typeof maquinas.forEach(() => {}));
// console.log(maquinas.find(maquina => maquina.id === 3));
// console.log(maquinas.filter(maquina => maquina.status === "Ativa"));

// // EXERCÍCIO 8 - Investigar erros
// const maquinaBusca = maquinas.find(maquina => maquina.id === 30);
// console.log(maquinaBusca);

// console.log(typeof maquinas[0].id);
// console.log(typeof "2");

// // EXERCÍCIO 9 - Tratar erro de leitura
// try {
//   const arquivo = fs.readFileSync("maquinas.json", "utf8");
//   const registros = JSON.parse(arquivo);
//   console.log(`Registros carregados: ${registros.length}`);
// } catch (erro) {
//   console.log("Não foi possível carregar os dados.");
//   console.log(erro.message);
// // }

// // Desafio A - Desafio A - Fundamental. Exiba uma linha para cada máquina no padrão ID | Nome | Status. Utilize o array carregado do JSON.

// console.log("Maquinas Cadastradas")
// console.log("\nID | Nome      | Status");
// maquinas.forEach(maquina => {
//     console.log(`${maquina.id} | ${maquina.nome} | ${maquina.status}`);
// });

// // Desafio B - Intermediário. Leia um ID de uma variável, localize a máquina e mostre o setor. Se não existir, apresente uma mensagem amigável.
// const id = 2;
// const maquinaAchada = maquinas.find(maquina => maquina.id === id);
// if (maquinaAchada === undefined) {
//     console.log("\nMaquina nao encontrada. Informe um id funcional.");
// } else {
//     console.log("---".repeat(10))
//     console.log(`Busca por ID: '${id}'`)
//     console.log(`\nID: ${maquinaAchada.id}`);
//     console.log(`Nome: ${maquinaAchada.nome}`);
//     console.log(`Setor: ${maquinaAchada.setor}`);
//     console.log(`Status: ${maquinaAchada.status}`);
// };

// // Desafio C - Intermediário. Crie uma variável com o nome de um setor. Exiba quantas máquinas pertencem a ele e os nomes encontrados.
// const nomeSetor = "Estamparia";
// const maquinaPorSetor = maquinas.filter(maquina => maquina.setor === nomeSetor);

// if (maquinaPorSetor[0] === undefined) {
//     console.log("\nMaquina nao encontrada.");
// } else {
//     console.log("---".repeat(8));
//     console.log(`Busca por setor: '${nomeSetor}'`);
//     console.log(`Quantidade de maquinas: ${maquinaPorSetor.length}`)
//     for (let m of maquinaPorSetor) {
//         console.log(`\nID: ${m.id}`);
//         console.log(`Nome: ${m.nome}`);
//         console.log(`Setor: ${m.setor}`);
//         console.log(`Status: ${m.status}`);
//     };
// };

// // Desafio D - Avançado. Crie uma função que receba um status por parâmetro e devolva o array filtrado. Teste com status existente e inexistente.
// function receberStatus(status) {
//     const maquinasEncontradas = maquinas.filter(maquina => maquina.status === status);
    
//     if (maquinasEncontradas[0] === undefined) {
//         console.log("\nMaquina nao encontrada.");
//     } else {
//         console.log("---".repeat(8));
//         console.log(`Maquinas com status '${status}'`)
//         for (let m of maquinasEncontradas) {
//             console.log(`\nID: ${m.id}`);
//             console.log(`Nome: ${m.nome}`);
//             console.log(`Setor: ${m.setor}`);
//         };
//     };
// };

// receberStatus("Ativa"); // Existente - exibe o array formatado
// receberStatus("aRiVo") // Inexistente - exibe 'Maquina nao encontrada.'

// // Desafio E - Transferência. Abra o projeto oficial da atividade no Classroom e identifique quais estruturas e métodos deste laboratório são úteis para implementar as funções pedidas. Não copie o laboratório sem adaptar ao formato dos dados reais.
