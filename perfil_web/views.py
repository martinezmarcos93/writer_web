from django.shortcuts import render
from perfil_web.models import inicio
# Create your views here.
def index(request):
    inicio = inicio.objects.first()
    return render(request, 'perfil_web/index.html', {'inicio': inicio})