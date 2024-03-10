const data = document.currentScript.dataset;
//console.log(data);
const iphones = data.iphones;

// Convertir el string en un array de JavaScript
var dataArray = JSON.parse(iphones.replace(/'/g, '"'));
//console.log(dataArray)
// Obtener elementos del DOM
var capacitySelect = document.querySelector('#capacitySelect');
var colorSelect = document.querySelector('#colorSelect');
//elemento de la imagen por su id

// Puedes utilizar 'dataFromDjango' en tu código JavaScript
var selectedCapacity;
// Escuchar cambios en la capacidad
capacitySelect.addEventListener('change', function() {
    selectedCapacity = capacitySelect.value - 1;
    //console.log('Capacidad seleccionada:', selectedCapacity);
    // Actualizar el precio en el DOM
    priceSpan.textContent = dataArray[selectedCapacity][1] + " Gs";

});

// Escuchar cambios en el color
var imagen = document.getElementById("imagenPerfil");
const num = data.num;
const modelo = data.modelo;
var color;
//console.log(num, modelo);
function cambiarColor(elemento) {
    // Obtenemos las clases del elemento clicado
    const clases = elemento.className.split(' ');
    // Buscamos la segunda clase (índice 1) y la utilizamos como color
    color = clases[1];
    // Utilizar template literals de JavaScript para concatenar las partes de la ruta
    const rutaImagen = `/static/img/colores/${num}${modelo}/${color}.jpg`;
    //console.log(rutaImagen);
    // Cambia el atributo src con la nueva ruta de la imagen
    imagen.src = rutaImagen;
    // Aquí puedes realizar acciones específicas para cambiar el color seleccionado.
    //console.log('Color seleccionado:', color);
    // También puedes actualizar el estilo de tus productos u otros elementos según el color seleccionado.
}

function consultarStock(){
    selectedCapacity = capacitySelect.value - 1;
    
    //console.log(dataArray[selectedCapacity][2])
    if (color){
        var enlaceWhatsApp = 'https://wa.me/+595985110487' + '?text=' + encodeURIComponent(`Hola, quisiera consultar el stock del iPhone ${num} ${modelo} de ${dataArray[selectedCapacity][2]} en color ${color}. Muchas Gracias!`);
    } else{
        var enlaceWhatsApp = 'https://wa.me/+595985110487' + '?text=' + encodeURIComponent(`Hola, quisiera consultar el stock del iPhone ${num} ${modelo} de ${dataArray[selectedCapacity][2]}. Muchas Gracias!`);
    }
    
     // Abre el enlace en una nueva pestaña o ventana
    window.open(enlaceWhatsApp, '_blank');
}
