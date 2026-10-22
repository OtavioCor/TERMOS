const entrada = require('readline-sync')
const manutencao = require('./funcoesManutencao')

console.log("--- SISTEMA MODULAR DE MANUTENCAO ---")

const nome = entrada.question("Digite o nome da maquina: ")
const vdp = entrada.questionFloat("Digite o valor das pecas: ")
const hds = entrada.questionFloat("Digite as hora de servico: ")
const ultima = entrada.questionInt("Digite a quantos meses foi a ultima manutencao: ")

const maoDeObra = manutencao.calcularMaoDeObra(hds)
const total = manutencao.calcularTotal(vdp, maoDeObra)
const garantia = manutencao.verificarGarantia(ultima)

console.log("----- RELATORIO -----")
console.log(`Maquina: ${nome}\nMao de obra: ${maoDeObra}\nValor das pecas: ${vdp}\nTotal: ${total}\nSituacao da garantia: ${garantia}`)
