from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def random(request):
    return HttpResponse("Hola estas en random")

def mierda(request):
    return HttpResponse("Hola estas en mierdas")