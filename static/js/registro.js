
function leerDatosRegistro() {

    const usuario = document.getElementById("usuario").value;
    const correo = document.getElementById("correo").value;
    const password = document.getElementById("password").value;
    const confirmarPassword = document.getElementById("confirmar_password").value;

    if (password !== confirmarPassword) {

        alert("Las contraseñas no coinciden.");

        return;
    }

    //prepara los valores para poder colocarlos en la url
    const usuarioUrl = encodeURIComponent(usuario);
    const correoUrl = encodeURIComponent(correo);
    const passwordUrl = encodeURIComponent(password);
    const confirmarUrl = encodeURIComponent(confirmarPassword);

    //direccion que recibirá django, template literal
    const url = `/registrar/${usuarioUrl}/${correoUrl}/${passwordUrl}/${confirmarUrl}/`;

    //direccion actual del navegador
    window.location.href = url;

}

function mostrarPasswordRegistro() {

    const password =
        document.getElementById("password");

    const confirmarPassword =
        document.getElementById("confirmar_password");


    if (password.type === "password") {

        password.type = "text";
        confirmarPassword.type = "text";

    } else {

        password.type = "password";
        confirmarPassword.type = "password";
    }
}

