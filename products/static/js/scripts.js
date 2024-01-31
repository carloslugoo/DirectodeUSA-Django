const data = document.currentScript.dataset;
console.log(data);
const iphones = data.iphones;

// Convertir el string en un array de JavaScript
var dataArray = JSON.parse(iphones.replace(/'/g, '"'));
console.log(dataArray)
// Obtener elementos del DOM
var capacitySelect = document.querySelector('#capacitySelect');
var colorSelect = document.querySelector('#colorSelect');
//elemento de la imagen por su id

// Puedes utilizar 'dataFromDjango' en tu código JavaScript

// Escuchar cambios en la capacidad
capacitySelect.addEventListener('change', function() {
    var selectedCapacity = capacitySelect.value - 1;
    console.log('Capacidad seleccionada:', selectedCapacity);
    // Actualizar el precio en el DOM
    priceSpan.textContent = dataArray[selectedCapacity][1] + " Gs";

});

// Escuchar cambios en el color
var imagen = document.getElementById("imagenPerfil");
const modelo = data.modelo;
console.log(modelo);
function cambiarColor(elemento) {
    // Obtenemos las clases del elemento clicado
    const clases = elemento.className.split(' ');
    // Buscamos la segunda clase (índice 1) y la utilizamos como color
    const color = clases[1];
    // Utilizar template literals de JavaScript para concatenar las partes de la ruta
    const rutaImagen = `/static/img/colores/${modelo}/${color}.jpg`;
    console.log(rutaImagen);
    // Cambia el atributo src con la nueva ruta de la imagen
    imagen.src = rutaImagen;
    // Aquí puedes realizar acciones específicas para cambiar el color seleccionado.
    console.log('Color seleccionado:', color);
    // También puedes actualizar el estilo de tus productos u otros elementos según el color seleccionado.
}
