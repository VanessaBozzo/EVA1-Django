from django.shortcuts import render
#Se importa una herramienta de django llamada HttpResponse, su trabajo es 
#devolver una respuesta http al navegador 
from django.http import HttpResponse

# Template (es una clase de django) permite convertir el texto del archivo 
# html en un template que django pueda procesar.
# Context es la clase que permite preparar los datos que queremos enviar a Template
# contiene clave : valor, y esas claves son las que aparecen en html en {{}}
from django.template import Template, Context

#Mas adelante se cambia Temple y Context por loader, es una herramienta de django para cargar Templates
from django.template import loader


usuarios_registrados = []


def inicioTemplateContext(request):

    archivo = open(
        "miproyecto/plantillas/inicio.html",
        encoding="utf-8"
    )

    contenido = archivo.read()

    #estructura html Clase Template
    tmp = Template(contenido)

    ctx = Context({
        #datos
        #clave  :    valor
        "titulo": "Template y Context",
        "mensaje": "Plantilla cargada usando Template y Context"
    })

    #procesa        #metodo del objeto de Template
    documento = tmp.render(ctx)

    archivo.close()

    return HttpResponse(documento)


# funcion python normal
# request, es la peticion que django entrega automaticamente a la view.
# cuando en el navegador se escribe http://127.0.0.1:8000/usuarios/, el navegador 
# esta diciendo: django, quiero acceder a esta direccion, django crea información 
# sobre esa peticion y se la entrega a la funcion inicio
def inicio(request):
    #devuelve al navegador este texto como respuesta
    #return HttpResponse("Modulo de usuario funcionando")

    #El Loader se encarga de buscar y cargar la plantilla, va a settings
    plantilla = loader.get_template("inicio.html")
    
    #relaciona las claves con variable plantilla
    documento = plantilla.render({
        "titulo": "Sistema de Usuario",
        "mensaje": "Modulo de usuario funcionando"
    })
    
    return HttpResponse(documento)


# misma funcion de arriba. Lo único que cambiará será cómo cargamos y devolvemos el Template.
# request, peticion que recibió la view desde el navegador cuando se quiere visitar /usuarios
def inicioShortcut(request):
    
    #dicionario
    contexto = {
        "titulo": "Sistema de usuarios",
        "mensaje": "Template cargado con shortcut render"
    }
    
    # render, django carga la plantilla, aplica los datos y prepara una respuesta para el navegador
    # request, peticion de arriba
    # inicio.html nombre del template que se quiere cargar, django sabe donde buscar gracias a que se configuró
    # en la etapa anterior, en settings, dirs
    return render(request, "inicio.html", contexto)
    # Devuelve al navegador la plantilla inicio.html, procesada con los datos de contexto, para responder a esta request



def inicioHerencia(request):
    
    contexto = {
        "titulo": "Herencia de templates",
        "mensaje": "Esta información viene desde la palntilla hija"
    }

    return render(request, "inicio_herencia.html", contexto)


#cargar registro
def registro(request):
    
    contexto = {
        "titulo": "Registro de usuario"
    }
    
    return render(request, "registro.html", contexto)



def registrarUsuario(request, usuario, correo, password, confirmar_password):
    
    #lista
    errores = []
    
    
    #validar que las contraseñas coincidan
    if password != confirmar_password:
        errores.append("Las contraseñas no coinciden")
    
    
    #validar minimo 8 caracteres
    if len(password) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres")
    
        
    #validar al menos una mayuscula
    tiene_mayuscula = False
    
    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
            
    if not tiene_mayuscula:
        errores.append("La contraseña debe contener al menos una letra mayúscula")
        

    # Validar al menos un número
    tiene_numero = False

    for caracter in password:
        if caracter.isdigit():
            tiene_numero = True

    if not tiene_numero:
        errores.append(
            "La contraseña debe contener al menos un número."
        )


    # Validar usuario y correo únicos
                            #arriba  
    for usuario_guardado in usuarios_registrados:

        if usuario_guardado["usuario"] == usuario:
            errores.append(
                "El nombre de usuario ya está registrado."
            )

        if usuario_guardado["correo"] == correo:
            errores.append(
                "El correo electrónico ya está registrado."
            )


    # Guardar solamente si no existen errores
    if not errores:

        nuevo_usuario = {
            "usuario": usuario,
            "correo": correo,
            "password": password,
            "intentos": 0,
            "bloqueado": False
        }

        usuarios_registrados.append(nuevo_usuario)
        

    contexto = {
        "usuario": usuario,
        "correo": correo,
        "errores": errores
    }
    

    return render(request, "resultado_registro.html", contexto)        
    

#cargar login
def login(request):

    contexto = {
        "titulo": "Inicio de sesión"
    }

    return render(request, "login.html", contexto)
    
    

def autenticarUsuario(request, usuario, password):

    usuario_encontrado = None

    # Buscar el usuario registrado
    for usuario_guardado in usuarios_registrados:

        if usuario_guardado["usuario"] == usuario:
            usuario_encontrado = usuario_guardado

    contexto = {
        "usuario": usuario,
        "mensaje": ""
    }

    # Caso 1: el usuario no existe
    if usuario_encontrado is None:

        contexto["mensaje"] = "El usuario no existe."

    # Caso 2: el usuario ya estaba bloqueado
    elif usuario_encontrado["bloqueado"]:

        contexto["mensaje"] = (
            "Clave bloqueada. "
            "Ha superado el máximo de intentos permitidos."
        )

    # Caso 3: contraseña incorrecta
    elif usuario_encontrado["password"] != password:

        usuario_encontrado["intentos"] += 1

        # Si llegó al tercer intento
        if usuario_encontrado["intentos"] >= 3:

            usuario_encontrado["bloqueado"] = True

            contexto["mensaje"] = (
                "Clave bloqueada. "
                "Ha superado el máximo de intentos permitidos."
            )

        # Si todavía no llega a tres intentos
        else:

            contexto["mensaje"] = (
                "Contraseña incorrecta. Intento "
                + str(usuario_encontrado["intentos"])
                + " de 3."
            )

    # Caso 4: usuario y contraseña correctos
    else:

        usuario_encontrado["intentos"] = 0

        contexto["mensaje"] = "Bienvenido, " + usuario


    return render(request, "resultado_login.html", contexto)

    

    