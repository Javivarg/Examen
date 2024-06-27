// Array para almacenar los usuarios creados
let usuariosGuardados = JSON.parse(localStorage.getItem('usuarios'));

console.log(localStorage.getItem("usuarios"))
console.log(usuariosGuardados)


// Función para iniciar sesión
function iniciarSesion() {
    // Obtener valores de los campos del formulario
    let nombre = document.getElementById('inputUsuario').value;
    let contraseña = document.getElementById('inputPassword').value;

    // Buscar el usuario en el array de usuarios
    let usuarioEncontrado = usuariosGuardados.find(usuariosGuardados => usuariosGuardados.nombre === nombre && usuariosGuardados.contraseña === contraseña);

    // Verificar si se encontró el usuario
    if (usuarioEncontrado) {
        document.getElementById('inputUsuario').value = '';
        document.getElementById('inputPassword').value = '';
        window.location.href = "index.html";
        alert("Inicio de sesión exitoso.");

    } else {
        alert("Usuario o contraseña incorrectos.");

    }
    
}

// Asociar las funciones a los botones
document.getElementById('btnIniciarSesion').addEventListener('click', iniciarSesion);

