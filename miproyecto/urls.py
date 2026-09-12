"""
URL configuration for miproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#importar la view. Desde el archivo views.py de la app usuarios, tráeme la función inicio, y las demás
from usuarios.views import inicioTemplateContext, inicio, inicioShortcut, inicioHerencia, registro, registrarUsuario, login, autenticarUsuario


urlpatterns = [
    path('', registro),
    path('admin/', admin.site.urls),
    path('template-context/', inicioTemplateContext),
    # 'usuarios/' es la direccion, inicio (referencia a la funcion en views) es la view 
    # que queremos ejecutar.
    # /usuarios/  ->  inicio()
    path('usuarios/',inicio),
    path('shortcut/', inicioShortcut),
    path('herencia/', inicioHerencia),
    path('registro/', registro),
    path('registrar/<usuario>/<correo>/<password>/<confirmar_password>/', registrarUsuario),
    path('login/', login),
    path('ingresar/<usuario>/<password>/', autenticarUsuario)
]

