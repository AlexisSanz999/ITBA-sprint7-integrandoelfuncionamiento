from re import template
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    #ej1
    '''return HttpResponse("Hello, world. You're at the polls index.")'''
    # ej2
    '''html_response = "<h1>Bienvenidos a mi sitio de prueba</h1>"
    for i in range(10):
        html_response += "<p>Línea " + str(i) + "</p>"
    return HttpResponse(html_response)'''
    #ej3
    return render(request, 'polls\index.html')