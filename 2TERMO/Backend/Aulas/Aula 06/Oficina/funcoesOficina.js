function calcularOrcamento(precoPeca, horasTrabalho){
    const valorHora = 85.00;
    const totalMaoDeObra = horasTrabalho * valorHora
    return precoPeca + totalMaoDeObra
}

function verificarGarantia(meses) {
    if (meses <= 3){
        return "Dentro da Garantia";
    } else {
        return "Garantia Expirada";
    }
}

function Desconto(valorTotal){
    return valorTotal * 0.95;
}
// module.exports - Possibilita a relação entre sistemas
module.exports = {
    calcularOrcamento, 
    verificarGarantia,
    Desconto
} 