
function leerDatosLogin() {

    const usuario = document.getElementById("login_usuario").value;
    const password = document.getElementById("login_password").value;


    const usuarioUrl = encodeURIComponent(usuario);
    const passwordUrl = encodeURIComponent(password);

    const url = `/ingresar/${usuarioUrl}/${passwordUrl}/`;

    window.location.href = url;
}