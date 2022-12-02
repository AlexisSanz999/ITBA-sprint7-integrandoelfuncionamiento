from django.shortcuts import render
from .models import Articulo

# Create your views here.

def home(request):
    articulos = Articulo.objects.all()
    contex = {"articulos": articulos}
    return render(request, "articulos/home.html", contex)
