document.addEventListener('DOMContentLoaded', function() {
    const precioButtons = document.querySelectorAll('.precio-btn');
    const listaProductos = document.getElementById('listaProductos');
    const precioTotalElement = document.getElementById('precioTotal');
    const vaciarCarritoBtn = document.getElementById('vaciarCarritoBtn');
    let carrito = cargarCarritoDesdeLocalStorage() || {};

    // Cargar productos del carrito cuando la página se carga
    actualizarVentanaEmergente();

    precioButtons.forEach(button => {
        button.addEventListener('click', function() {
            const precio = parseInt(this.getAttribute('data-precio'));
            const productoNombre = this.parentElement.querySelector('.card-title').textContent;

            if (carrito[productoNombre]) {
                carrito[productoNombre].cantidad++;
            } else {
                carrito[productoNombre] = {
                    precio: precio,
                    cantidad: 1
                };
            }
            console.log(carrito[productoNombre].precio)

            actualizarVentanaEmergente();
            guardarCarritoEnLocalStorage(carrito);
            // Mostrar una alerta
            alert(`¡${productoNombre} agregado al carrito!`);
        });
    });

    vaciarCarritoBtn.addEventListener('click', function() {
        carrito = {};
        actualizarVentanaEmergente();
        guardarCarritoEnLocalStorage(carrito);
    });

    function actualizarVentanaEmergente() {
        listaProductos.innerHTML = '';
        let total = 0;

        for (const productoNombre in carrito) {
            const producto = carrito[productoNombre];
            const listItem = document.createElement('li');
            listItem.textContent = `${productoNombre} x ${producto.cantidad}: $${(producto.precio * producto.cantidad).toFixed(2)}`;
            listaProductos.appendChild(listItem);
            total += producto.precio * producto.cantidad;
        }

        precioTotalElement.textContent = `Total: $${total.toFixed(2)}`;
    }

    function actualizarLista() {
        const listaProductos = document.getElementById('listaProductos');
        const precioTotalElement = document.getElementById('precioTotalElement');
        let total = 0;
    
        // Supongamos que 'carrito' es un objeto con los productos y sus detalles
        for (const productoNombre in carrito) {
            const producto = carrito[productoNombre];
            const listItem = document.createElement('li');
            listItem.textContent = `${productoNombre} x ${producto.cantidad}: $${(producto.precio * producto.cantidad).toFixed(2)}`;
            listaProductos.appendChild(listItem);
            total += producto.precio * producto.cantidad;
        }
    
        precioTotalElement.textContent = `Total: $${total.toFixed(2)}`;
    }
    
    // Llama a la función para actualizar la lista y el precio total
    actualizarLista();
    

    // Almacenar el carrito en localStorage
    function guardarCarritoEnLocalStorage(carrito) {
        localStorage.setItem('carrito', JSON.stringify(carrito));
    }

    // Cargar el carrito desde localStorage
    function cargarCarritoDesdeLocalStorage() {
        const carritoString = localStorage.getItem('carrito');
        if (carritoString) {
            return JSON.parse(carritoString);
        }
        return null;
    }
});
