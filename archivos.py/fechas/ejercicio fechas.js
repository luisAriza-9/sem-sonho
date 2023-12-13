

function calcularMulta() {
  const fechaEntregaPactada = new Date(document.getElementById("fechaEntregaPactada").value);
  const fechaEntregaReal = new Date(document.getElementById("fechaEntregaReal").value);
  let diasPasados = (fechaEntregaReal - fechaEntregaPactada) / (1000 * 60 * 60 * 24);
  let multa = 0;
  if (diasPasados <= 3) {
    multa = diasPasados * 7000;
  } else if (diasPasados > 4) {
    multa = 10000;
    alert("No se permitirá el préstamo por 6 meses.");
  }
  document.getElementById("diasPasados").innerHTML = diasPasados;
  document.getElementById("multa").innerHTML = multa;
}



