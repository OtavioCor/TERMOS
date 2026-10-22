const entrada = require('readline-sync');


pecasDefeituosas = []

const qtd = entrada.questionInt('Quantas pecas com defeito foram encontradas: ')

for (let i = 0; i < qtd; i++){
    let serie = entrada.question(`Digite a serie da peca ${i + 1}: `)
    pecasDefeituosas.push(serie)
}

console.log(pecasDefeituosas)
