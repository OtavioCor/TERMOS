function checarTemperatura(valor){
    if (valor > 40) {
        return "ALERTA: Caldeira Superaquecida"
    } else {
        return "Temperatura adequada"
    }
}

function checarUmidade(valor){
    if (valor < 20) {
        return "ALERTA: Ar muito seco"
    } else {
        return "Umidade adequada"
    }
}

module.exports = {
    checarTemperatura,
    checarUmidade
}