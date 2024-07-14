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

            actualizarVentanaEmergente();
            guardarCarritoEnLocalStorage(carrito);
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
            const listItem = document.createElement('tr');
            listItem.className = 'producto-item';
    
            const productoText = document.createElement('td');
            
            productoText.textContent = `${productoNombre}`;
            listItem.appendChild(productoText);

            const productoCant = document.createElement('td');
            
            productoCant.textContent = `${producto.cantidad}`;
            listItem.appendChild(productoCant);

            const productoPrecio = document.createElement('td');
            
            productoPrecio.textContent = `$${(producto.precio * producto.cantidad)}`;
            listItem.appendChild(productoPrecio);
    
            const btnGroup = document.createElement('div');
            btnGroup.className = 'btn-group';
    
            const incrementButton = document.createElement('button');
            incrementButton.className = 'btn btn-success';
            incrementButton.textContent = '+';
            incrementButton.addEventListener('click', function() {
                carrito[productoNombre].cantidad++;
                actualizarVentanaEmergente();
                guardarCarritoEnLocalStorage(carrito);
            });
            btnGroup.appendChild(incrementButton);
    
            const decrementButton = document.createElement('button');
            decrementButton.className = 'btn btn-danger';
            decrementButton.textContent = '-';
            decrementButton.addEventListener('click', function() {
                carrito[productoNombre].cantidad--;
                if (carrito[productoNombre].cantidad === 0) {
                    delete carrito[productoNombre];
                }
                actualizarVentanaEmergente();
                guardarCarritoEnLocalStorage(carrito);
            });
            btnGroup.appendChild(decrementButton);
            
            listItem.appendChild(btnGroup);
            listaProductos.appendChild(listItem);
            total += producto.precio * producto.cantidad;
        }
    
        precioTotalElement.textContent = `Total: $${total}`;
    }
    

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
