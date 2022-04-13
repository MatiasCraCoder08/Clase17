"""ProyectoCoder27615 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ProyectoCoder27615.views import dia_de_hoy, saludo, saludo_con_nombre, anio_nacimiento, con_plantilla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('saludo/<nombre>', saludo_con_nombre),
    path('hoy/', dia_de_hoy),
    path('anio/<int:edad>', anio_nacimiento),
    path('', con_plantilla)
]
