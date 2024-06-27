let producto =[];
let productosSeleccionados = JSON.parse(localStorage.getItem('producto'))

/*function guardarProductos(){
    let nombreProducto = document.getElementById("nombreP").value;
    let precioProducto = document.getElementById("precioP").value;
    let cantidadProducto = 0;

    let nuevoProducto = {
        nombre : nombreProducto,
        precio : precioProducto,
        cantidad : cantidadProducto,
    }

    //agregar nuevo producto
    producto.push(nuevoProducto);
    ///localStorage.setItem('producto',JSON.stringify(producto))

    if(producto[nombreProducto]){
        producto[nombreProducto].cantidad++
        producto[nombreProducto].precio*=producto[nombreProducto].cantidad
    }else{
        producto[nombreProducto]={
            precio : precioProducto,
            cantidad : 1
        }
    }

    localStorage.setItem('producto',JSON.stringify(producto))
}*/

// Obtén el elemento con la clase "precio-btn"
const precioBtnElement = document.querySelector('.precio-btn');

// Agrega un event listener al botón
precioBtnElement.addEventListener('click', () => {
  // Obtén el elemento con la clase "card-title"
    const cardTitleElement = document.querySelector('.card-title');

    // Guarda los valores en variables locales
    const cardTitle = cardTitleElement.textContent;
    const precio = precioBtnElement.textContent;

    // Ahora puedes usar las variables "cardTitle" y "precio" según tus necesidades
    //console.log(`Título de la tarjeta: ${cardTitle}`);
    //console.log(`Precio: ${precio}`);

    let nuevoProducto = {
    nombre : cardTitleElement,
    precio : precio,
    cantidad : 0,
    }

    producto.push(nuevoProducto);

    if(producto[cardTitleElement]){
        producto[cardTitleElement].cantidad++
    }else{
        producto[cardTitleElement]={
            precio : precio,
            cantidad :1
        }
    }


    console.log(producto)
    localStorage.setItem('producto',JSON.stringify(producto))
    console.log(productosSeleccionados)
});

