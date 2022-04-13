from contextvars import Context
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola mundo!")


def dia_de_hoy(request):
    hoy = datetime.now()
    texto = f"Hoy es el día: {hoy}"
    return HttpResponse(texto)


def saludo_con_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre}")


def anio_nacimiento(request, edad):
    hoy = datetime.now()
    anio = hoy.year - edad
    return HttpResponse(f"Naciste aprox. en {anio}")


def con_plantilla(request):
    mi_html = open("/home/matiascra/Documents/Coderhouse/Curso 08-02-2022/Clase17/ProyectoCoder27615/ProyectoCoder27615/plantillas/plantilla.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(plantilla)
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)