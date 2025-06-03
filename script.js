const texto = "Experiencia Autodidacta";
let i = 0;
const titulo = document.getElementById("titulo");

function escribirTexto() {
  if (!titulo) return;  // <-- si no existe, corta acá

  if (i < texto.length) {
    titulo.innerHTML += texto.charAt(i);
    i++; 
    setTimeout(escribirTexto, 100); 
  }
}

escribirTexto();

console.log("script cargado y listo")
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('.acordeon-titulo').forEach(boton => {
    boton.addEventListener('click', () => {
      const panel = boton.nextElementSibling;

      if (panel.style.maxHeight && panel.style.maxHeight !== "0px") {
        // Está abierto, cerramos
        panel.style.maxHeight = null;
        panel.style.padding = "0 16px";
      } else {
        // Cerramos todos primero
        document.querySelectorAll('.acordeon_p').forEach(p => {
          p.style.maxHeight = null;
          p.style.padding = "0 16px";
        });
        // Abrimos el que clickeamos
        panel.style.maxHeight = panel.scrollHeight + "px";
        panel.style.padding = "12px 16px";
      }
    });
  });
});


  