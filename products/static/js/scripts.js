const data = document.currentScript.dataset;
console.log(data);
const iphones = data.iphones;

// Convertir el string en un array de JavaScript
var dataArray = JSON.parse(iphones.replace(/'/g, '"'));
console.log(dataArray)
// Obtener elementos del DOM
var capacitySelect = document.querySelector('#capacitySelect');
var colorSelect = document.querySelector('#colorSelect');

// Ahora, 'dataFromDjango' es un array de JavaScript con los valores del vector 'data'

// Puedes utilizar 'dataFromDjango' en tu código JavaScript

// Escuchar cambios en la capacidad
capacitySelect.addEventListener('change', function() {
    var selectedCapacity = capacitySelect.value - 1;
    console.log('Capacidad seleccionada:', selectedCapacity);
    // Actualizar el precio en el DOM
    priceSpan.textContent = dataArray[selectedCapacity][1] + " Gs";

});

// Escuchar cambios en el color
colorSelect.addEventListener('change', function() {
    var selectedColor = colorSelect.value;
    console.log('Color seleccionado:', selectedColor);
});
