// Array para almacenar los usuarios creados
let usuarios = [];
console.log(localStorage.getItem("usuarios"))
// Función para crear un nuevo usuario


$(document).ready(function() {
    $("#registroForm").submit(function(event) {
        event.preventDefault();

        var nombre = $("#inputNombre").val();
        var email = $("#inputEmailNuevo").val();
        var contraseña = $("#inputPasswordNuevo").val();
        var confirmarContra = $("#inputConfirmarPassword").val();

        if (nombre.length < 3 || nombre.length > 20) {
            alert("El Nombre de Usuario debe tener entre 3 y 20 caracteres.");
            return;
        }

        if (!email.includes('@')) {
            alert("El correo electrónico debe contener al menos un símbolo '@'.");
            return;
        }

        if (contraseña.length < 3 || contraseña.length > 20) {
            alert("La Contraseña debe tener entre 3 y 20 caracteres.");
            return;
        }

        if (contraseña !== confirmarContra) {
            alert("Las contraseñas no coinciden.");
            return;
        }

        // Crear objeto de usuario
        let nuevoUsuario = {
            nombre: nombre,
            email: email, // Corregir aquí
            contraseña: contraseña
        };

        // Agregar usuario al array de usuarios
        usuarios.push(nuevoUsuario);
        localStorage.setItem('usuarios', JSON.stringify(usuarios));

        // Limpiar campos de entrada
        document.getElementById('inputNombre').value = '';
        document.getElementById('inputEmailNuevo').value = '';
        document.getElementById('inputPasswordNuevo').value = '';
        document.getElementById('inputConfirmarPassword').value = '';

        // Mostrar mensaje de éxito después de limpiar los campos
        alert("¡Registro exitoso!");
    });
});



