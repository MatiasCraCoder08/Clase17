from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
# Importo settings para poder usar una variable del archivo settings.py
from django.conf import settings


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
    # Con ruta absoluta al archivo .html
    # mi_html = open("/home/matiascra/Documents/Coderhouse/Curso 08-02-2022/Clase17/ProyectoCoder27615/ProyectoCoder27615/plantillas/plantilla.html")
    
    # Uso una variable del archivo settings.py que tiene la ruta al proyecto. No
    # es exactamente un string y puedo concatenarle texto con la "/"
    mi_html = open(settings.BASE_DIR / "ProyectoCoder27615/plantillas/plantilla.html")
    # Creo una plantilla con los datos del html
    plantilla = Template(mi_html.read())
    mi_html.close()

    # Necesito un "contexto" para poder renderizar una plantilla a algo que se
    # pueda mostrar.
    mi_contexto = Context(plantilla)
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
