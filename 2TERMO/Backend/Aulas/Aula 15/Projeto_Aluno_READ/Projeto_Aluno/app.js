// PROJETO DO ALUNO - complete as funções abaixo.
// Execute com: npm start
const fs = require('node:fs');
const caminho = require('node:path');
const ARQUIVO = caminho.join(__dirname, 'maquinas.json');

function carregarMaquinas() {
  // TODO 1: ler ARQUIVO com fs.readFileSync(ARQUIVO, 'utf8').
  const texto = fs.readFileSync("maquinas.json", "utf8");

  // TODO 2: converter o texto JSON em array com JSON.parse(...).
  const maquina = JSON.parse(texto);

  // TODO 3: retornar o array.
  return maquina
  throw new Error('Implementar carregarMaquinas');
}

function listarMaquinas(maquinas) {
  // TODO 4: percorrer com forEach e apresentar id, nome e status.

  maquinas.forEach((maquina, indice) => {
  console.log(`${indice + 1}. ${maquina.nome} - ${maquina.setor} - ${maquina.status} - ${maquina.horasUso/n}`);
  });

  throw new Error('Implementar listarMaquinas');
}

function buscarPorId(maquinas, id) {
  // TODO 5: encontrar com find(). O ID recebido deve ser número.
  return maquinas.find(maquina => maquina.id === id);

  throw new Error('Implementar buscarPorId');
}

function filtrarPorStatus(maquinas, status) {
  // TODO 6: retornar um novo array com filter().
  return maquinas.filter(maquina => maquina.status === status
  );
  throw new Error('Implementar filtrarPorStatus');
}

function filtrarPorSetor(maquinas, setor) {
  // DESAFIO: retornar máquinas do setor informado.
  return maquinas.filter(maquina => maquina.setor === setor
  );
  throw new Error('Implementar filtrarPorSetor');
}

function executar() {
  try {
  // TODO 7: chamar carregarMaquinas, listarMaquinas e fazer consultas.
  // Exemplos a testar: id 3, id 99, status 'manutencao'.

  
  carregarMaquinas()
  listarMaquinas()
  buscarPorId()
  filtrarPorStatus()
  filtrarPorSetor()

  console.log('Sistema de consultas industriais - CRUD READ');
  }catch (erro) {
    console.error('Erro ao ler ou consultar o arquivo:', erro.message);
    process.exitCode = 1;
  }
}


if (require.main === module) executar();
module.exports = { carregarMaquinas, listarMaquinas, buscarPorId, filtrarPorStatus, filtrarPorSetor };




