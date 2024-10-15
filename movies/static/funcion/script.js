const toggleButton = document.getElementById("toggleButton");
const container = document.getElementById("container");

const menuIcon = document.querySelector('.menu-icon');
const nav = document.querySelector('nav');

menuIcon.addEventListener('click', () => {
    nav.classList.toggle('show');
});
// Verifica el color de fondo almacenado en localStorage
const currentBackgroundColor = localStorage.getItem("backgroundColor");
if (currentBackgroundColor === "black") {
    container.classList.add("black-bg");
    toggleButton.checked = true; // Marca el checkbox si el fondo es negro
} else {
    container.classList.add("white-bg");
    toggleButton.checked = false; // Desmarca el checkbox si el fondo es blanco
}

// Evento de clic para alternar el color de fondo
toggleButton.addEventListener("change", () => {
    // Alterna las clases entre 'black-bg' y 'white-bg'
    container.classList.toggle("black-bg");
    container.classList.toggle("white-bg");

    // Guarda la preferencia en localStorage
    if (container.classList.contains("black-bg")) {
        localStorage.setItem("backgroundColor", "black");
    } else {
        localStorage.setItem("backgroundColor", "white");
    }
});
