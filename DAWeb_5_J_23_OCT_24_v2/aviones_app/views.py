from django.shortcuts import render
from .models import Aviones
def listadoAviones(request):
    losaviones=Aviones.objects.all()
    return render(request, "gestionarAviones.html",{"misaviones":losaviones})
