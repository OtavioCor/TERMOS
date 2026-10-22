const entrada = require('readline-sync')

documento = []

console.log("--- REGISTRO DE OPERADORES ---")
for (i = 1; i <= 5; i++){
    let nome = entrada.question("Digite o nome: ")
    documento.push(nome)
}

console.log("--- LISTA REGISTRADA ---")
for (i = 0; i < documento.length; i++) {
    console.log(`${i + 1}° Registro - ${documento[i]}`)
}
