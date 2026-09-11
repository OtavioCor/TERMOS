const entrada = require('readline-sync')

documento = []

for (i = 1; i <= 5; i++){
    let nome = entrada.question("Digite o nome: ")
    documento.push(nome)
}

for (i = 0; i <= documento.length; i++) {
    console.log(`${i} - ${documento[i]}`)
}
