from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_tienda(request):
    return HttpResponse("<h1>Bienvenido a la tienda<h1>")